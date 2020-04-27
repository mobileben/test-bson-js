import bson
import json

# Below will not decode
#data = { 'key0': 'a', 'key1': [ 1, 2, 3 ], 'key2': 'b', 'key3': [ { 'k0': 'random', 'k1': 'string', 'k2': 'to use', 'k3': 3.145 }, { 'k0': 'other', 'k1': 'values', 'k2': 'here', 'k3': 0.0001}] }

# Below will not work with the following error
# Uncaught Error: buffer length 143 must === bson size 253
#   deserialize$1
#   deserialize$2
data = {  'key3': [ { 'k0': 'random', 'k1': 'string', 'k2': 'to use', 'k3': 3.145 }, { 'k0': 'other', 'k1': 'values', 'k2': 'here', 'k3': 0.0001}] }

# Below will decode properly and the resulting Javascript object is correct
#data = { 'key3': [ { 'k0': 'random', 'k1': 'string', 'k2': 'to use' }, { 'k0': 'other', 'k1': 'values', 'k2': 'here'}] }

# Below will decode, however the resulting Javascript object is incorrect (float values are wrong). This is the output in JS
# {"key3":[{"k0":1.8745098039215684,"k1":1.8745098039215684,"k2":1.825},{"k0":1.8745098039215684,"k1":1.8125,"k2":1.825}]}
#data = { 'key3': [ { 'k9': 'here', 'k0': 0.1, 'k1': 0.2, 'k2': 0.3 }, { 'k0': 0.4, 'k1': 0.5, 'k2': 0.6}] }

# Below will decode, however the resulting floating point numbers will be incorrect in the Javascript object
#data = { 'key3': { 'k9': 'here', 'k0': 0.1, 'k1': 0.2, 'k2': 0.3 } }

# Below will decode properly and the resulting Javascript object is correct
#data = { 'key3': { 'k9': 'here', 'k0': 1, 'k1': 2, 'k2': 3 } }

json_str = json.dumps(data)
print(json_str)

with open('test.bson', 'wb') as fp:
    encoded = bson.encode(data)
    fp.write(encoded)
