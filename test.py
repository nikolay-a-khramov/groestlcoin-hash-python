import groestlcoin_hash

data = b'\x00'
digest = groestlcoin_hash.getHash(data, len(data))
assert digest == b'\xe8r\x10\xb1\xe1\xd6t\xe6%?\x85\x82\x05\x9a;\xeaQa\xce\xf1\xe5\xb3-]\x06\xc5\xc3\x15P\xf9\xef*'

print("OK")