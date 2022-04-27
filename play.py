import base64, codecs
magic = 'aW1wb3J0IHRpbWUsIHN5cywgYXN5bmNpbywgb3MsIHJlcXVlc3RzCmZyb20gcGxheXdyaWdodF9zdGVhbHRoIGltcG9ydCBzdGVhbHRoLCBzdGVhbHRoX2FzeW5jCmZyb20gcGxheXdyaWdodC5hc3luY19hcGkgaW1wb3J0IFBsYXl3cmlnaHQsIGFzeW5jX3BsYXl3cmlnaHQsIFRpbWVvdXRFcnJvciBhcyBQbGF5d3JpZ2h0VGltZW91dEVycm9yCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUKZnJvbSBkb3RlbnYgaW1wb3J0IGxvYWRfZG90ZW52Cgp0cnk6CiAgICBvcy5ta2RpcigncmVzdWx0JykKZXhjZXB0OgogICAgcGFzcwoKY2IgPSAnJycKfD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CnwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfAp8ICAgIF9fX18gX19fIF9fXyBfICAgXyBfX19fICAgIF8gICAgX19fXyAgX19fX18gIHwKfCAgLyBfX18vIF8gXF8gX3wgXCB8IHwgX18gKSAgLyBcICAvIF9fX3x8IF9fX198ICB8CnwgfCB8ICB8IHwgfCB8IHx8ICBcfCB8ICBfIFwgLyBfIFwgXF9fXyBcfCAgX3wgICAgfAp8IHwgfF9ffCB8X3wgfCB8fCB8XCAgfCB8XykgLyBfX18gXCBfX18pIHwgfF9fXyAgIHwKfCAgXF9fX19cX19fL19fX3xffCBcX3xfX19fL18vICAgXF9cX19fXy98X19fX198ICB8CnwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfAp8ICAgICAgICAgICAgICAgIFZBTElEQVRPUiBDTEkgICAgICAgICAgICAgICAgICAgIHwKfCAgICAgICAgICAgICAgICAgICBYR2hvc3QgICAgICAgICAgICAgICAgICAgICAgICB8Cnw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fAonJycKCnByaW50KGYne2NifScpCgphc3luYyBkZWYgcnVuKHBsYXl3cmlnaHQ6IFBsYXl3cmlnaHQpIC0+IE5vbmU6CgogICAgdHJ5OgogICAgICAgIGxvYWRfZG90ZW52KCkKI'
love = 'PNtVPNtVPOvpz93p2IlVQ0tLKqunKDtpTkurKqlnJqbqP5wnUWioJy1oF5fLKIhL2tbXDbtVPNtVPNtVTAioaEyrUDtCFOuq2ScqPOvpz93p2IlYz5yq19wo250MKu0XTI4qUWuK2u0qUOsnTIuMTIlpm17W1ImMKVgDJqyoaDaBvNaGJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2APxtDKOjoTIKMJWYnKDiAGZ3YwZ2VPuYFSEAGPjtoTyeMFOUMJAeolxtD2ulo21yYmtmYwNhAQRjZl4kZGLtH2SzLKWcYmHmAl4mAvq9XDbtVPNtVPNtVTS3LJy0VUA0MJSfqTusLKA5ozZbL29hqTI4qPxXVPNtVPNtVPOjLJqyVQ0tLKqunKDtL29hqTI4qP5hMKqspTSaMFtcPvNtVPNtVPNtLKqunKDtpTSaMF5ao3EiXPWbqUEjpmbiY3Olol5wo2yhLzSmMF5wo20ip2yaoaIjY2yxqy9lMKS1nKWyMPVcPvNtVPNtVPNtMz5uoJHtCFOjLJqyYzkiL2S0o3VbVygjoTSwMJuioTEypw1pVxMcpaA0KSjtGzSgMIjvKFVcPvNtVPNtVPNtLKqunKDtMz5uoJHhqUyjMFtvFzuiozHvYPOxMJkurG01ZPxXVPNtVPNtVPOfozSgMFN9VUOuM2HhoT9wLKEipvtvJ3OfLJAynT9fMTIlCIjvGTSmqSkpVR5uoJIpVy0vXDbtVPNtVPNtVTS3LJy0VTkhLJ1yYaE5pTHbVxgyoz5yMTxvYPOxMJkurG01ZPxXVPNtVPNtVPOgLJjtCFOjLJqyYzkiL2S0o3VbVygjoTSwMJuioTEypw1pVayiqIkpDTI4LJ1joTIpKP5wo21pVy0vXDbtVPNtVPNtVTS3LJy0VT1uoP5znJkfXTLvr21unJkmsFVcPvNtVPNtVPNtpTSmqlN9VUOuM2HhoT9wLKEipvtvJ3OfLJAynT9fMTIlCIjvGJyhnJ11oIkpVQupKPOwnTSlLJA0MKWmKPWqVvxXVPNtVPNtVPOuq2ScqPOjLKA3YaE5pTHbVxggrapxJJS5ZQyNVlVfVTEyoTS5CGHjXDbtVPNtVPNtVTS3LJy0VUOuM2HhoT9wLKEipvtvnJ5jqKEoqUyjMG1pVzAbMJAeLz94KPWqVvxhL2uyL2fbXDbtVPNtVPNtVTS3LJy0VUOuM2HhoT9wLKEipvtvqTI4qQ1QpzIuqTHtLJ4tDJAwo3IhqPVcYzAfnJAeXPxXVPNtVPNtVPO0pax6PvNtVP'
god = 'AgICAgICAgIGh0bWwgPSBhd2FpdCBwYWdlLmlubmVyX3RleHQoJ1tjbGFzcz1cImFsZXJ0XFwgYWxlcnQtZXJyb3JcXCBhbGVydC1kYW5nZXJcIl0nKQogICAgICAgICAgICBzID0gaHRtbC5zcGxpdCgiXG4iKQogICAgICAgICAgICBpZiBzWzFdID09ICdBbiBhY2NvdW50IGFscmVhZHkgZXhpc3RzIHdpdGggdGhpcyBlbWFpbCBhZGRyZXNzLic6CiAgICAgICAgICAgICAgICB0eCA9IG9wZW4oInJlc3VsdC92YWxpZC50eHQiLCAiYSsiKQogICAgICAgICAgICAgICAgdHgud3JpdGUoJ1xuJykKICAgICAgICAgICAgICAgIHR4LndyaXRlbGluZXMoZiJ7bWFpbHN9IikKICAgICAgICAgICAgICAgIHR4LmNsb3NlKCkKICAgICAgICAgICAgICAgIHByaW50KGYie0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7bWFpbHN9ID17Rm9yZS5MSUdIVENZQU5fRVh9IFZhbGlkIikKICAgICAgICAgICAgICAgIGF3YWl0IGNvbnRleHQuY2xvc2UoKQogICAgICAgICAgICAgICAgYXdhaXQgYnJvd3Nlci5jbG9zZSgpCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICB0eCA9IG9wZW4oInJlc3VsdC9kaWUudHh0IiwgImErIikKICAgICAgICAgICAgdHgud3JpdGUoJ1xuJykKICAgICAgICAgICAgdHgud3JpdGVsaW5lcyhmInttYWlsc30iKQogICAgICAgICAgICB0eC5jbG9zZSgpCiAgICAgICAgICAgIHByaW50KGYie0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7bWFpbHN9ID17Rm9yZS5MSUdIVFJFRF9FWH0gRGllIikgCiAgICAgICAgICAgIGF3YWl0IGNvbnRleHQuY2xvc2UoKQogICAgICAgICAgICBhd2FpdCBicm93c2VyLmNsb3NlKCkKICAgIGV4Y2VwdCBQbGF5d3JpZ2h0VGltZW91dEVycm9yOgogICAgICAgIHByaW50KGYie0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7bWFpbHN9ID17Rm9yZS5MSUdIVFlFTExPV19FWH0gQmFkIFByb3h'
destiny = '5VvxXVPNtVPNtVPO0rPN9VT9jMJ4bVaWyp3IfqP9vLJDgpUWirUxhqUu0VvjtVzReVvxXVPNtVPNtVPO0rP53pzy0MFtaKT4aXDbtVPNtVPNtVUE4YaqlnKEyoTyhMKZbMvW7oJScoUA9VvxXVPNtVPNtVPO0rP5woT9mMFtcPvNtVPNtVPNtLKqunKDtL29hqTI4qP5woT9mMFtcPvNtVPNtVPNtLKqunKDtLaWiq3Aypv5woT9mMFtcPtbXPzSmrJ5wVTEyMvOgLJyhXPxtYG4tGz9hMGbXVPNtVTSmrJ5wVUqcqTttLKA5ozAspTkurKqlnJqbqPtcVTSmVUOfLKy3pzyanUD6PvNtVPNtVPNtLKqunKDtpaIhXUOfLKy3pzyanUDcPvNtVPNXPaqcqTtto3OyovumrKZhLKWaqyfkKFjtW3VaXFOuplOfnKA0BtbtVPNtMJ1unJjtCFOfnKA0YaWyLJDbXF5mpTkcqTkcozImXPxXVPNtVUEiqTSfVQ0toTIhXTIgLJyfXDbXMz9lVT1unJkmVTyhVTIgLJyfBtbtVPNtLKOcn2I5VQ0tpzIkqJImqUZhM2I0XPqbqUEjpmbiY3Wuql5anKEbqJW1p2IlL29hqTIhqP5wo20inJ1gn3IhMF9iL3VioJScov90pzyuoP1upTxhqUu0WlxhqTI4qNbtVPNtnJLtVzZ5BJVlMwVkYGMzLGtgATIwMP1uBGHlYJLmZ2H2ZTMyLmVlBPVtnJ4tLKOcn2I5BtbtVPNtVPNtVTMipvOgLJyfplOcovOyoJScoQbXVPNtVPNtVPNtVPNtLKA5ozAcol5lqJ4boJScovtcXDbtVPNtMJkmMGbXVPNtVPNtVPOjpzyhqPuzW3gTo3WyYxkWE0uHI0uWIRIsEIu9KT5oX117Ez9lMF5ZFHqVISWSES9SJU0tJJ91pvOOpTyeMKxtFTSmVRI4pTylMJE7Ez9lMF5ZFHqVISqVFIESK0ILsFOoX10aXDbtVPNtVPNtVUOlnJ50XTLar0MipzHhGRyUFSEKFRyHEI9SJU1oX117Ez9lMF5ZFHqVIRqFEHIBK0ILsFOUMKDtpUWyoJy1oFOOpTyeMKxtqT8aXDbtVPNtVPNtVUOlnJ50XTLar0MipzHhGRyUFSEKFRyHEI9SJU1oX117Ez9lMF5ZFHqVIRqFEHIBK0ILsFOHMJkyM3WuoFO7Ez9lMF5ZFHqVIRWZIHIsEIu9DTu1oaEypacsMTywMKgTo3WyYxkWE0uHI0uWIRIsEIu9VSfeKFpcPvNtVPNtVPNtMKucqPtc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
