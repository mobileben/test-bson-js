# Overview
This is simple test case to try and save a dictionary as BSON. The intent is to use this data as either embedded data or as a loaded file in Javascript. I am using Webpack and Typescript for development on the JS-side

Note that this is my first usage of BSON. `bsondump` can dump the data as JSON. And I can decode it in Python.


I've created an SO question here: https://stackoverflow.com/questions/61448282/converting-bson-data-saved-in-file-to-javascript-object/61448920?noredirect=1#comment108701976_61448920

And an issue on `js-bson` here: https://github.com/mongodb/js-bson/issues/357

# createbson.py
This creates the test data (`test.bson`). This relies on `pymongo` for `bson`.

# Javascript
I am installing bson using the following command. 

```
npm install bson
```

Which is this package:
https://www.npmjs.com/package/bson

I have found a couple of ways I can can load the file

## Embedded
I have found I can embed the data using `raw-loader` loader. This allows me to have a line such as this

```
import tdat from '!!raw-loader!assets/test.bson'
```

## XmlHttpRequest
Another method is to use `XMLHttpRequest`

```
let xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = () => {
    if (xmlHttp.status == 200 && xmlHttp.readyState == 4) {
        // Data is in xmlHttp.responseText
    }
};
xmlHttp.open("GET", 'assets/test.bson');
xmlHttp.send();
```

# Problem
I do not seem to be able to convert the embedded data/loaded file into a Javascript object. I've tried permutations of `deserialize`, `serialize`, `stringify`, and `parse` but have encountered various errors or exceptions.

Currently looking for the right method. 

I believe my generated data is correct, but also don't know for certain. I am using the basis that `bsondump` was successful at dumping it as an indicator the file is correct.

# Updates

The following code tests out the two ways to load the file

```
import tdat from '!!raw-loader!scripts/data/test.bson'

let xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = () => {
    if (xmlHttp.status == 200 && xmlHttp.readyState == 4) {
        const buf = Buffer.from(xmlHttp.responseText, 'binary');
        //const buf = Buffer.from(xmlHttp.responseText);
        console.log(buf);
        const dat = deserialize(buf, {});
        console.log(JSON.stringify(dat));
    }
};
xmlHttp.open("GET", 'assets/test.bson');
xmlHttp.send();

const tbuf = Buffer.from(tdat, 'binary');
const other_dat = deserialize(tbuf, {});
console.log(JSON.stringify(other_dat));
```

# Sample Bad Case
The following python dict

```
data = {  'key3': [ { 'k0': 'random', 'k1': 'string', 'k2': 'to use', 'k3': 3.145 }, { 'k0': 'other', 'k1': 'values', 'k2': 'here', 'k3': 0.0001}] }
```

Results in the following error 

```
Uncaught Error: buffer length 143 must === bson size 253
  deserialize$1	
  deserialize$2	
```

Running `bsondump` results in the following (`--type=json` and then `--type=debug`):

```
{"key3":[{"k0":"random","k1":"string","k2":"to use","k3":{"$numberDouble":"3.145"}},{"k0":"other","k1":"values","k2":"here","k3":{"$numberDouble":"0.0001"}}]}
2020-04-26T17:28:17.044-0700	1 objects found
```

``` 
--- new object ---
	size : 143
		key3
			type:    4 size: 138
			--- new object ---
				size : 132
					0
						type:    3 size: 65
						--- new object ---
							size : 62
								k0
									type:    2 size: 15
								k1
									type:    2 size: 15
								k2
									type:    2 size: 15
								k3
									type:    1 size: 12
					1
						type:    3 size: 62
						--- new object ---
							size : 59
								k0
									type:    2 size: 14
								k1
									type:    2 size: 15
								k2
									type:    2 size: 13
								k3
									type:    1 size: 12
```

# I've encountered the following

- Must use `binary` as the encoding for converting the string to a `Buffer`
- Depending on the data, some will decode, while others will fail due to an `Uncaught error` where it indicates the buffer is smaller than the expected bson size.
- When it does decode, floating point values are wrong. Integers are fine.

The Python code lists some cases that work and don't work.
