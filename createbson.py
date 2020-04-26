import bson

data = { 'key0': 'a', 'key1': [ 1, 2, 3 ], 'key2': 'b' }
with open('test.bson', 'wb') as fp:
    encoded = bson.encode(data)
    fp.write(encoded)