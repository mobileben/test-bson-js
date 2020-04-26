import bson

data = { 'key0': 'a', 'key1': [ 1, 2, 3 ], 'key2': 'b', 'key3': [ { 'k0': 'random', 'k1': 'string', 'k2': 'to use', 'k3': 3.145 }, { 'k0': 'other', 'k1': 'values', 'k2': 'here', 'k3': 0.0001}] }
with open('test.bson', 'wb') as fp:
    encoded = bson.encode(data)
    fp.write(encoded)