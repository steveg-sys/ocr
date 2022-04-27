import base64, codecs
magic = 'ZnJvbSB0aW1lIGltcG9ydCBzbGVlcAppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHN5cywgb3MsIHppcGZpbGUKaW1wb3J0IHByb3h5CmZyb20gcHl2aXJ0dWFsZGlzcGxheSBpbXBvcnQgRGlzcGxheQppbXBvcnQgY29uY3VycmVudC5mdXR1cmVzCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUKZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY29tbW9uLmtleXMgaW1wb3J0IEtleXMKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY29tbW9uLmFjdGlvbl9jaGFpbnMgaW1wb3J0IEFjdGlvbkNoYWlucwpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5zdXBwb3J0LndhaXQgaW1wb3J0IFdlYkRyaXZlcldhaXQKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydCBpbXBvcnQgZXhwZWN0ZWRfY29uZGl0aW9ucyBhcyBFQwpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jaHJvbWUub3B0aW9ucyBpbXBvcnQgT3B0aW9ucwpmcm9tIHNlbGVuaXVtLmNvbW1vbi5leGNlcHRpb25zIGltcG9ydCBUaW1lb3V0RXhjZXB0aW9uCmZyb20gc2VsZW5pdW1fc3RlYWx0aCBpbXBvcnQgc3RlYWx0aAppbXBvcnQgY2hyb21lZHJpdmVyX2JpbmFyeQoKZGlzcGxheSA9IERpc3BsYXkodmlzaWJsZT0wLCBzaXplPSg4MDAsIDYwMCkpCmRpc3BsYXkuc3RhcnQoKQoKCiMjY2IgPSAnJycgICAgICAKIyMgICAgICAgICApICggICAgICAgKSAgICAgICAgICAgICAgKCAgICAgICAgCiMjICAgKCAgKCAvKCApXCApICggLyggICAoICAgICggICAgIClcICkgICAgIAojIyAgIClcIClcKCl8KCkvKCApXCgpKSggKVwgICApXCAgICgoKS8oKCAgICAKIyMgKCgoX3woXylcIC8oXyl8KF8pXCApKChffCgoKF8pKCAgLyhfKSlcICAgCiMjIClcX19fICgoX3xfKSkgIF8oKF98KF8pXyApXCBfIClcKF8pKSgoXykgIAojIygoLyBfXy8gXyBcXyBffHwgXHwgfHwgXyApKF8pX1woXykgX198IF9ffCAKIyMgfCAoX3wgKF8pIHwgfCB8IC5gIHx8IF8gXCAvIF8gXCBcX18gXCBffCAgCiMjICBcX19fXF9fXy9fX198fF98XF98fF9fXy8vXy8gXF9cfF9fXy9fX198IAojIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAojIyAgICAgICAgICAgICAgICBWQUxJREFUT1IgQ0xJICAgICAgICAgICAgICAgICAgICAKIyMnJycKY2IgPSAnJycKfD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CnwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfAp8ICAgIF9fX18gX19fIF9fXyBfICAgXyBfX19fICAgIF8gICAgX19fXyAgX19fX18gIHwKfCAgLyBfX18vIF8gXF8gX3wgXCB8IHwgX18gKSAgLyBcICAvIF9fX3x8IF9fX198ICB8CnwgfCB8ICB8IHwgfCB8IHx8ICBcfCB8ICBfIFwgLyBfIFwgXF9fXyBcfCAgX3wgICAgfAp8IHwgfF9ffCB8X3wgfCB8fCB8XCAgfCB8XykgLyBfX18gXCBfX18pIHwgfF9fXyAgIHwKfCAgXF9fX19cX19fL19fX3xffCBcX3xfX19fL18vICAgXF9cX19fXy98X19fX198ICB8CnwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfAp8ICAgICAgICAgICAgICAgIFZBTElEQVRPUiBDTEkgICAgICAgICAgICAgICAgICAgIHwKfCAgICAgICAgICAgICAgICAgICBYR2hvc3QgICAgICAgICAgICAgICAgICAgICAgICB8Cnw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fAonJycKCnByaW50KGYne0ZvcmUuTElHSFRNQUdFTlRBX0VYfXtjYn17Rm9yZS5SRVNFVH1cbicpCgp0cnk6CiAgZW1haWxpc3QgPSBbXQoKICBtYWlsaXN0ID0gb3BlbihpbnB1dCgiSW5wdXQgWW91ciBMaXN0OiAiKSkKICBsaW1lID0gbWFpbGlzdC5yZWFkKCkuc3BsaXRsaW5lcygpCiAgdG90ID0gbGVuKGxpbWUpCiAgZm9yIGxpbmUgaW4gbGltZToKICAgIGVtYWlsaXN0LmFwcGVuZChsaW5lKQpleGNlcHQ6CiAgcHJpbnQoIldyb25nIGlucHV0IG9yIGxpc3Qgbm90IGZvdW5kISI'
love = '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'
god = 'ljYXRlLWVycm9ycycpCiAgICBvcHQuYWRkX2FyZ3VtZW50KCItLWRpc2FibGUtY29va2llLWVuY3J5cHRpb24iKQogICAgb3B0LmFkZF9hcmd1bWVudCgiLS1kaXNhYmxlLWJsaW5rLWZlYXR1cmVzPUF1dG9tYXRpb25Db250cm9sbGVkIikKICAgIG9wdC5hZGRfYXJndW1lbnQoInVzZXItYWdlbnQ9TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzgzLjAuNDEwMy4xMTYgU2FmYXJpLzUzNy4zNiIpICAgIAogICAgZHJpdmVyID0gd2ViZHJpdmVyLkNocm9tZShvcHRpb25zPW9wdCkKICAgIHN0ZWFsdGgoZHJpdmVyLAogICAgICAgIGxhbmd1YWdlcz1bImVuLVVTIiwgImVuIl0sCiAgICAgICAgdmVuZG9yPSJHb29nbGUgSW5jLiIsCiAgICAgICAgcGxhdGZvcm09IldpbjMyIiwKICAgICAgICB3ZWJnbF92ZW5kb3I9IkludGVsIEluYy4iLAogICAgICAgIHJlbmRlcmVyPSJJbnRlbCBJcmlzIE9wZW5HTCBFbmdpbmUiLAogICAgICAgIGZpeF9oYWlybGluZT1UcnVlLAogICAgKQogICAgdHJ5OgogICAgICBhcGlrZXkgPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9pbW1rdW5lL29jci9tYWluL2FwaS50eHQnKS50ZXh0CiAgICAgIGlmICJlNGFkYjFiNS1iNWRmLTQ1YmQtODQ5My0zYzg2Y2ExNGEzNjIiIGluIGFwaWtleToKICAgICAgICAgIHRyeToKICAgICAgICAgICAgICBkcml2ZXIuaW1wbGljaXRseV93YWl0KDE1KQogICAgICAgICAgICAgIGRyaXZlci5nZXQoJ2h0dHBzOi8vcHJvLmNvaW5iYXNlLmNvbS9zaWdudXAvaWR2X3JlcXVpcmVkJykKICAgICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LklELCAidXNlcl9maXJzdF9uYW1lIikuc2VuZF9rZXlzKCJKaG9uIikKICAgICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LklELCAidXNlcl9sYXN0X25hbWUiKS5zZW5kX2tleXMoIktlbm5lZHkiKQogICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnQoQnkuSUQsICJ1c2VyX2VtYWlsIikuY2xpY2soKQogICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnQoQnkuSUQsICJ1c2VyX2VtYWlsIikuc2VuZF9rZXlzKGVtYWlscykKICAgICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LklELCAidXNlcl9hY2NlcHRlZF91c2VyX2FncmVlbWVudCIpLmNsaWNrKCkgICAKICAgICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LklELCAidXNlcl9wYXNzd29yZCIpLnNlbmRfa2V5cygiS1R5QnZ3aGQ3ODMmQCMiKQogICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnQoQnkuTkFNRSwgImNvbW1pdCIpLmNsaWNrKCkKICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgIGVsZW1lbnQgPSBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LkNTU19TRUxFQ1RPUiwgIi5hbGVydCIpCiAgICAgICAgICAgICAgICAgIHRleHQgPSBlbGVtZW50LmdldF9hdHRyaWJ1dGUoJ2lubmVySFRNTCcpCiAgICAgICAgICAgICAgICAgIGh0bWwgPSBCZWF1dGlmdWxTb3VwKHRleHQsICdodG1sLnBhcnNlcicpCiAgICAgICAgICAgICAgICAgIHJlYWR5ID0gaHRtbC5nZXRfdGV4dCgpCiAgICAgICAgICAgICAgICAgIGlmICJBbiBhY2NvdW50IGFscmVhZHkgZXhpc3RzIHdpdGggdGhpcyBlbWFpbCBhZGRyZXNzLiIgaW4gcmVhZHk6CiAgICAgICAgICAgICAgICAgICAgICBwcmludChmJ3tGb3JlLkxJR0hUV0hJVEVfRVh9WyNde0ZvcmUuTElHSFRHUkVFTl9FWH0ge2VtYWlsc30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRDWUFOX0VYfSBWYWxpZCcpCiAgICAgICAgICAgICAgICAgICAgICB0eCA9IG9wZW4oJ3Jlc3VsdC92YWxpZC50eHQnLCAnYSsnKQogICAgICAgICAgICAgICAgICAgICAgdHgud3JpdGUoJ1xuJykKICAgICAgICAgICAgICAgICAgICAgIHR4LndyaXRlbGluZXMoZW1haWxzKQogICAgICAgICAgICAgICAgICAgICAgdHguY2xvc2UoKSAgCiAgICAgICAgICAgICAgICAgICAgICBkcml2ZXIucXVpdCgpCiAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgI'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
