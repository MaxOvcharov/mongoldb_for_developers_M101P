import base64
code="CmltcG9ydCBweW1vbmdvCmltcG9ydCB1cmxsaWIyCmltcG9ydCB1cmxsaWIKaW1wb3J0IGNvb2tpZWxpYgppbXBvcnQgcmFuZG9tCmltcG9ydCByZQppbXBvcnQgc3RyaW5nCmltcG9ydCBzeXMKaW1wb3J0IGdldG9wdAoKIyB0aGlzIGlzIGEgdmFsaWRhdGlvbiBwcm9ncmFtIHRvIG1ha2Ugc3VyZSB0aGF0IHRoZSBibG9nIHdvcmtzIGNvcnJlY3RseS4KIyBJZiB5b3UgYXJlIHJlYWRpbmcgdGhpcyBpbiBjbGVhciB0ZXh0LCB5b3UgYXJlIHByb2JhYmx5IHZpb2xhdGluZyB0aGUgaG9ub3IgY29kZQoKIyBpbml0IHRoZSBnbG9iYWwgY29va2llIGphcgpjaiA9IGNvb2tpZWxpYi5Db29raWVKYXIoKQojIGRlY2xhcmUgdGhlIHZhcmlhYmxlcyB0byBjb25uZWN0IHRvIGRiCmNvbm5lY3Rpb24gPSBOb25lCmRiID0gTm9uZQp3ZWJob3N0ID0gImxvY2FsaG9zdDo4MDgyIgptb25nb3N0ciA9ICJtb25nb2RiOi8vbG9jYWxob3N0OjI3MDE3IgpkYl9uYW1lID0gImJsb2ciCgojIHRoaXMgc2NyaXB0IHdpbGwgY2hlY2sgdGhhdCBob21ld29yayAzLjIgaXMgY29ycmVjdAoKIyBtYWtlcyBhIGxpdHRsZSBzYWx0CmRlZiBtYWtlX3NhbHQobik6CiAgICBzYWx0ID0gIiIKICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgIHNhbHQgPSBzYWx0ICsgcmFuZG9tLmNob2ljZShzdHJpbmcuYXNjaWlfbGV0dGVycykKICAgIHJldHVybiBzYWx0CgoKIyB0aGlzIGlzIGEgdmFsaWRhdGlvbiBwcm9ncmFtIHRvIG1ha2Ugc3VyZSB0aGF0IHRoZSBibG9nIHdvcmtzIGNvcnJlY3RseS4KCmRlZiBjcmVhdGVfdXNlcih1c2VybmFtZSwgcGFzc3dvcmQpOgogICAgCiAgICBnbG9iYWwgY2oKCiAgICB0cnk6CiAgICAgICAgcHJpbnQgIlRyeWluZyB0byBjcmVhdGUgYSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICB1cmwgPSAiaHR0cDovL3swfS9zaWdudXAiLmZvcm1hdCh3ZWJob3N0KQoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJlbWFpbCIsIiIpLCgidXNlcm5hbWUiLHVzZXJuYW1lKSwgKCJwYXNzd29yZCIscGFzc3dvcmQpLCAoInZlcmlmeSIscGFzc3dvcmQpXSkKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwsIGRhdGE9ZGF0YSkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcih1cmxsaWIyLkhUVFBDb29raWVQcm9jZXNzb3IoY2opKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICB1c2VycyA9IGRiLnVzZXJzCiAgICAgICAgIyBjaGVjayB0aGF0IHRoZSB1c2VyIGlzIGluIHVzZXJzIGNvbGxlY3Rpb24KICAgICAgICB1c2VyID0gdXNlcnMuZmluZF9vbmUoeydfaWQnOnVzZXJuYW1lfSkKICAgICAgICBpZiAodXNlciA9PSBOb25lKToKICAgICAgICAgICAgcHJpbnQgIkNvdWxkIG5vdCBmaW5kIHRoZSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUsICJpbiB0aGUgdXNlcnMgY29sbGVjdGlvbi4iCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIHByaW50ICJGb3VuZCB0aGUgdGVzdCB1c2VyICIsIHVzZXJuYW1lLCAiIGluIHRoZSB1c2VycyBjb2xsZWN0aW9uIgoKICAgICAgICAjIGNoZWNrIHRoYXQgdGhlIHVzZXIgaGFzIGJlZW4gYnVpbHQKICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKCJXZWxjb21lXHMrIisgdXNlcm5hbWUpCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBjcmVhdGUgYSB1c2VyLCBoZXJlIGlzIHRoZSBvdXRwdXQgd2UgZ290XG4iCiAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgCiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCiAgICAgICAgcmV0dXJuIEZhbHNlCgoKZGVmIHRyeV90b19sb2dpbih1c2VybmFtZSwgcGFzc3dvcmQpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGxvZ2luIGZvciB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICB1cmwgPSAiaHR0cDovL3swfS9sb2dpbiIuZm9ybWF0KHdlYmhvc3QpCgogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoInVzZXJuYW1lIix1c2VybmFtZSksICgicGFzc3dvcmQiLHBhc3N3b3JkKV0pCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIodXJsbGliMi5IVFRQQ29va2llUHJvY2Vzc29yKGNqKSkKICAgICAgICBmID0gb3BlbmVyLm9wZW4ocmVxdWVzdCkKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBsb2dpbgogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIldlbGNvbWVccysiKyB1c2VybmFtZSkKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBsb2dpbiwgaGVyZSBpcyB0aGUgb3V0cHV0IHdlIGdvdFxuIgogICAgICAgIHByaW50IHJlc3VsdAogICAgICAgIHJldHVybiBGYWxzZQogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByZXR1cm4gRmFsc2UKCgpkZWYgYWRkX2Jsb2dfcG9zdCh0aXRsZSxwb3N0LHRhZ3MpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIHN1Ym1pdCBhIHBvc3Qgd2l0aCB0aXRsZSAiLCB0aXRsZQogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoImJvZHkiLHBvc3QpLCAoInN1YmplY3QiLHRpdGxlKSwgKCJ0YWdzIix0YWdzKV0pCiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vbmV3cG9zdCIuZm9ybWF0KHdlYmhvc3QpCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgICMgY2hlY2sgZm9yIHN1Y2Nlc3NmdWwgbG9naW4KICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKHRpdGxlICsgIi4rIiArIHBvc3QsIHJlLkRPVEFMTCkKCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKCiAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gcG9zdCwgaGVyZSBpcyB0aGUgb3V0cHV0IHdlIGdvdFxuIgogICAgICAgIHByaW50IHJlc3VsdAogICAgICAgIHJldHVybiBGYWxzZQoKICAgIGV4Y2VwdDoKICAgICAgICBwcmludCAidGhlIHJlcXVlc3QgdG8gIiwgdXJsLCAiIGZhaWxlZCwgc28geW91ciBibG9nIG1heSBub3QgYmUgcnVubmluZy4iCiAgICAgICAgcmFpc2UKCiAgICAgICAgcmV0dXJuIEZhbHNlCgpkZWYgYWRkX2Jsb2dfY29tbWVudCh0aXRsZSxwb3N0KToKCiAgICB0cnk6CiAgICAgICAgcHJpbnQgIlRyeWluZyB0byBzdWJtaXQgYSBibG9nIGNvbW1lbnQgZm9yIHBvc3Qgd2l0aCB0aXRsZSIsIHRpdGxlCiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vbmV3Y29tbWVudCIuZm9ybWF0KHdlYmhvc3QpCiAgICAgICAgCiAgICAgICAgZG9jID0ge30KICAgICAgICBjaGVja19tb25nb19mb3JfcG9zdCh0aXRsZSwgcG9zdCwgZG9jKQoKICAgICAgICBwZXJtYWxpbmsgPSBkb2NbJ2RvYyddWydwZXJtYWxpbmsnXQoKICAgICAgICBjb21tZW50X25hbWUgPSBtYWtlX3NhbHQoMTIpCiAgICAgICAgY29tbWVudF9ib2R5ID0gbWFrZV9zYWx0KDEyKQoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJjb21tZW50TmFtZSIsY29tbWVudF9uYW1lKSwgKCJjb21tZW50Qm9keSIsY29tbWVudF9ib2R5KSwgKCJwZXJtYWxpbmsiLHBlcm1hbGluayldKQogICAgICAgIHJlcXVlc3QgPSB1cmxsaWIyLlJlcXVlc3QodXJsPXVybCwgZGF0YT1kYXRhKQogICAgICAgIGNqLmFkZF9jb29raWVfaGVhZGVyKHJlcXVlc3QpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIoKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICAjIGNoZWNrIGZvciBzdWNjZXNzZnVsIGFkZGl0aW9uIG9mIGNvbW1lbnQgb24gcGFnZQogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUodGl0bGUgKyAiLisiICsgcG9zdCwgcmUuRE9UQUxMKQoKICAgICAgICBpZiBub3QgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gZmluZCB0aGUgY29tbWVudCB3ZSBwb3N0ZWQgYXQgdGhlICAiLCB1cmwsICIgaGVyZSBpcyB3aGF0IHdlIGdvdCIKICAgICAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgICAgIHJldHVybiBGYWxzZQoKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBhZGRpdGlvbiBvZiBjb21tZW50Li5yZXRyaWV2ZSB0aGUgZG9jIGFnYWluCiAgICAgICAgaWYobm90IGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlLCBwb3N0LCBkb2MpKToKICAgICAgICAgICAgcHJpbnQgIkNvdWxkIG5vdCBmaW5kIGNvbW1lbnQgaW4gZGF0YWJhc2UiCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIAogICAgICAgIGZvdW5kID0gRmFsc2UKICAgICAgICBpZiAoJ2NvbW1lbnRzJyBpbiBkb2NbJ2RvYyddKToKICAgICAgICAgICAgZm9yIGNvbW1lbnQgaW4gZG9jWydkb2MnXVsnY29tbWVudHMnXToKICAgICAgICAgICAgICAgIGlmIChjb21tZW50Wydib2R5J10gPT0gY29tbWVudF9ib2R5IGFuZCBjb21tZW50WydhdXRob3InXSA9PSBjb21tZW50X25hbWUpOgogICAgICAgICAgICAgICAgICAgIGZvdW5kID0gVHJ1ZQoKICAgICAgICByZXR1cm4gZm91bmQKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKCiMgZ3JhYnMgdGhlIGJsb2cgaW5kZXggYW5kIGNoZWNrcyB0aGF0IHRoZSBwb3N0cyBhcHBlYXIgaW4gdGhlIHJpZ2h0IG9yZGVyCmRlZiBjaGVja19ibG9nX2luZGV4KHRpdGxlMSwgdGl0bGUyKToKCiAgICB0cnk6CiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vIi5mb3JtYXQod2ViaG9zdCkKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGdyYWIgdGhlIGJsb2cgaG9tZSBwYWdlIGF0IHVybCAiLCB1cmwKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgICMgY2hlY2sgZm9yIHN1Y2Nlc3NmdWwgbG9naW4KICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKHRpdGxlMiArICIuKyIgKyB0aXRsZTIsIHJlLkRPVEFMTCkKCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKCiAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gcmVhZCB0aGUgYmxvZyBpbmRleCBhdCAiLCB1cmwsICIgaGVyZSBpcyB3aGF0IHdlIGdvdCIKICAgICAgICBwcmludCByZXN1bHQKICAgICAgICByZXR1cm4gRmFsc2UKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKIyBjaGVjayB0aGF0IGEgcGFydGljdWxhciBibG9nIHBvc3QgaXMgaW4gdGhlIGNvbGxlY3Rpb24KZGVmIGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlLCBib2R5LCBkb2N1bWVudCk6CiAgICAKICAgIHBvc3RzID0gZGIucG9zdHMKICAgIHRyeToKICAgICAgICBwb3N0ID0gcG9zdHMuZmluZF9vbmUoeyd0aXRsZSc6dGl0bGUsICdib2R5Jzpib2R5fSkKICAgICAgICBpZiAocG9zdCBpcyBOb25lKToKICAgICAgICAgICAgcHJpbnQgIkNhbid0IGZpbmQgcG9zdCB3aXRoIHRpdGxlICIsIHRpdGxlLCAiIGluIGNvbGxlY3Rpb24iCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGRvY3VtZW50Wydkb2MnXSA9IHBvc3QKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJjYW4nIHF1ZXJ5IE1vbmdvREIuLmlzIGl0IHJ1bm5pbmc/IgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKIyBjb21tYW5kIGxpbmUgYXJnIHBhcnNpbmcgdG8gbWFrZSBmb2xrcyBoYXBweSB3aG8gd2FudCB0byBydW4gYXQgbW9uZ29sYWJzIG9yIG1vbmdvaHEKIyB0aGlzIGZ1bmN0aW9ucyB1c2VzIGdsb2JhbCB2YXJzIHRvIGNvbW11bmljYXRlLiBmb3JnaXZlIG1lLgpkZWYgYXJnX3BhcnNpbmcoYXJndik6CgogICAgZ2xvYmFsIHdlYmhvc3QKICAgIGdsb2JhbCBtb25nb3N0cgogICAgZ2xvYmFsIGRiX25hbWUKCiAgICB0cnk6CiAgICAgICAgb3B0cywgYXJncyA9IGdldG9wdC5nZXRvcHQoYXJndiwgIi1wOi1tOi1kOiIpCiAgICBleGNlcHQgZ2V0b3B0LkdldG9wdEVycm9yOgogICAgICAgIHByaW50ICJ1c2FnZSB2YWxpZGF0ZS5weSAtcCB3ZWJob3N0IC1tIG1vbmdvQ29ubmVjdFN0cmluZyAtZCBkYXRhYmFzZU5hbWUiCiAgICAgICAgcHJpbnQgIlx0d2ViaG9zdCBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdCh3ZWJob3N0KQogICAgICAgIHByaW50ICJcdG1vbmdvQ29ubmVjdGlvblN0cmluZyBkZWZhdWx0IHRvIHswfSIuZm9ybWF0KG1vbmdvc3RyKQogICAgICAgIHByaW50ICJcdGRhdGFiYXNlTmFtZSBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdChkYl9uYW1lKQogICAgICAgIHN5cy5leGl0KDIpCiAgICBmb3Igb3B0LCBhcmcgaW4gb3B0czoKICAgICAgICBpZiAob3B0ID09ICctaCcpOgogICAgICAgICAgICBwcmludCAidXNhZ2UgdmFsaWRhdGUucHkgLXAgd2ViaG9zdCAtbSBtb25nb0Nvbm5lY3RTdHJpbmcgLWQgZGF0YWJhc2VOYW1lIgogICAgICAgICAgICBzeXMuZXhpdCgyKQogICAgICAgIGVsaWYgb3B0IGluICgiLXAiKToKICAgICAgICAgICAgd2ViaG9zdCA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBIVFRQIGhvc3QgdG8gYmUgIiwgd2ViaG9zdAogICAgICAgIGVsaWYgb3B0IGluICgiLW0iKToKICAgICAgICAgICAgbW9uZ29zdHIgPSBhcmcKICAgICAgICAgICAgcHJpbnQgIk92ZXJyaWRpbmcgTW9uZ29EQiBjb25uZWN0aW9uIHN0cmluZyB0byBiZSAiLCBtb25nb3N0cgogICAgICAgIGVsaWYgb3B0IGluICgiLWQiKToKICAgICAgICAgICAgZGJfbmFtZSA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBNb25nb0RCIGRhdGFiYXNlIHRvIGJlICIsIGRiX25hbWUKICAgICAgICAgICAgCgoKIyBtYWluIHNlY3Rpb24gb2YgdGhlIGNvZGUKZGVmIG1haW4oYXJndik6CiAgICAgICAgICAgIAogICAgYXJnX3BhcnNpbmcoYXJndikKICAgIGdsb2JhbCBjb25uZWN0aW9uCiAgICBnbG9iYWwgZGIKCiAgICBwcmludCAiV2VsY29tZSB0byB0aGUgSFcgMy4yIGFuZCBIVyAzLjMgdmFsaWRhdGlvbiB0ZXN0ZXIiCgogICAgIyBjb25uZWN0IHRvIHRoZSBkYiAobW9uZ29zdHIgd2FzIHNldCBpbiBhcmdfcGFyc2luZykKICAgIGNvbm5lY3Rpb24gPSBweW1vbmdvLk1vbmdvQ2xpZW50KG1vbmdvc3RyKQogICAgZGIgPSBjb25uZWN0aW9uW2RiX25hbWVdCiAgICAgICAgCiAgICB1c2VybmFtZSA9IG1ha2Vfc2FsdCg3KQogICAgcGFzc3dvcmQgPSBtYWtlX3NhbHQoOCkKCiAgICAgIyB0cnkgdG8gY3JlYXRlIHVzZXIKCiAgICBpZiAoY3JlYXRlX3VzZXIodXNlcm5hbWUsIHBhc3N3b3JkKSk6CiAgICAgICAgcHJpbnQgIlVzZXIgY3JlYXRpb24gc3VjY2Vzc2Z1bC4gIgogICAgICAgICAjIHRyeSB0byBsb2dpbgogICAgICAgIGlmICh0cnlfdG9fbG9naW4odXNlcm5hbWUsIHBhc3N3b3JkKSk6CiAgICAgICAgICAgIHByaW50ICJVc2VyIGxvZ2luIHN1Y2Nlc3NmdWwuIgogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50ICJVc2VyIGxvZ2luIGZhaWxlZCIKICAgICAgICAgICAgcHJpbnQgIk9kZCwgdGhpcyB3ZWVrcydzIGNvZGUgc2hvdWxkIGRvIHRoYXQgYXMgZ2l2ZW4iCiAgICAgICAgICAgIHN5cy5leGl0KDEpCgogICAgZWxzZToKICAgICAgICBwcmludCAiU29ycnksIHlvdSBoYXZlIG5vdCBzb2x2ZWQgaXQgeWV0LiIKICAgICAgICBzeXMuZXhpdCgxKQoKCiAgICAjIHRyeSB0byBjcmVhdGUgYSBibG9nIHBvc3QKICAgIHBvc3QxID0gbWFrZV9zYWx0KDMwKQogICAgdGl0bGUxID0gbWFrZV9zYWx0KDMwKQogICAgdGFnczEgPSBtYWtlX3NhbHQoNSkgKyAiLCAiICsgbWFrZV9zYWx0KDUpICsgIiwgIiArIG1ha2Vfc2FsdCg1KQoKCiAgICBpZiAoYWRkX2Jsb2dfcG9zdCh0aXRsZTEsIHBvc3QxLHRhZ3MxKSk6CiAgICAgICAgcHJpbnQgIlN1Ym1pc3Npb24gb2Ygc2luZ2xlIHBvc3Qgc3VjY2Vzc2Z1bCIKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlVuYWJsZSB0byBjcmVhdGUgYSBwb3N0IgogICAgICAgIHN5cy5leGl0KDEpCgoKICAgICMgdHJ5IHRvIGNyZWF0ZSBhIHNlY29uZCBibG9nIHBvc3QKICAgIHBvc3QyID0gbWFrZV9zYWx0KDMwKQogICAgdGl0bGUyID0gbWFrZV9zYWx0KDMwKQogICAgdGFnczIgPSBtYWtlX3NhbHQoNSkgKyAiLCAiICsgbWFrZV9zYWx0KDUpICsgIiwgIiArIG1ha2Vfc2FsdCg1KQoKICAgIGlmIChhZGRfYmxvZ19wb3N0KHRpdGxlMiwgcG9zdDIsdGFnczIpKToKICAgICAgICBwcmludCAiU3VibWlzc2lvbiBvZiBzZWNvbmQgcG9zdCBzdWNjZXNzZnVsIgogICAgZWxzZToKICAgICAgICBwcmludCAiVW5hYmxlIHRvIGNyZWF0ZSBzZWNvbmQgcG9zdCIKICAgICAgICBzeXMuZXhpdCgxKQoKICAgICMgbm93IGxldCdzIG1ha2Ugc3VyZSB0aGF0IGJvdGggcG9zdHMgYXBwZWFyIG9uIHRoZSBob21lIHBhZ2Ugb2YgdGhlIGJsb2csIGluIHRoZSBjb3JyZWN0IG9yZGVyCgogICAgaWYgKGNoZWNrX2Jsb2dfaW5kZXgodGl0bGUxLCB0aXRsZTIpKToKICAgICAgICBwcmludCAiQmxvY2sgaW5kZXggbG9va3MgZ29vZC4iCiAgICBlbHNlOgogICAgICAgIHByaW50ICJCbG9nIGluZGV4IGRvZXMgbm90IGhhdmUgdGhlIHBvc3RzIHByZXNlbnQsIG9yZGVyZWQgY29ycmVjdGx5IgogICAgICAgIHN5cy5leGl0KDEpCgoKICAgICMgY2hlY2sgZm9yIERCIGRhdGEgaW50ZWdyaXR5CiAgICBpZiAobm90IGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlMSwgcG9zdDEsIHt9KSk6CiAgICAgICAgcHJpbnQgIkNhbid0IGZpbmQgYmxvZyBwb3N0IGluIGJsb2cgZGIsIHBvc3RzIGNvbGxlY3Rpb24gd2l0aCB0aXRsZSAiLCB0aXRsZQogICAgICAgIHN5cy5leGl0KDEpCiAgICBlbHNlOgogICAgICAgIHByaW50ICJGb3VuZCBibG9nIHBvc3QgaW4gcG9zdHMgY29sbGVjdGlvbiIKCgogICAgcHJpbnQgIlRlc3RzIFBhc3NlZCBmb3IgSFcgMy4yLiBZb3VyIEhXIDMuMiB2YWxpZGF0aW9uIGNvZGUgaXMgODlqa2xmc2pybGsyMDlqZmtzMmoyZWsiCgogICAgIyBub3cgY2hlY2sgdGhhdCB5b3UgY2FuIHBvc3QgYSBjb21tZW50CiAgICBpZiAobm90IGFkZF9ibG9nX2NvbW1lbnQodGl0bGUxLHBvc3QxKSk6CiAgICAgICAgcHJpbnQgIkNhbid0IGFkZCBibG9nIGNvbW1lbnRzIChzbyBIVyAzLjMgbm90IHlldCBjb21wbGV0ZSkiCiAgICAgICAgc3lzLmV4aXQoMSkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlN1Y2Nlc3NmdWxseSBhZGRlZCBibG9nIGNvbW1lbnRzIgoKCiAgICBwcmludCAiVGVzdHMgUGFzc2VkIGZvciBIVyAzLjMuIFlvdXIgSFcgMy4zIHZhbGlkYXRpb24gY29kZSBpcyBqazEzMTB2bjJsa3YwajJrZjBqa2ZzIgogICAgCgoKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKHN5cy5hcmd2WzE6XSkKCgoKCgoKCg=="

# Compatible for Python 3.6
with open('validate_test.py', 'x') as f:
    f.write(base64.b64decode(code).decode())

# eval(compile(base64.b64decode(code), "<string>", 'exec'))
