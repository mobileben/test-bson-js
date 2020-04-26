# Overview
This is simple test case to try and save a dictionary as BSON. The intent is to use this data as either embedded data or as a loaded file in Javascript. I am using Webpack and Typescript for development on the JS-side

Note that this is my first usage of BSON. `bsondump` can dump the data as JSON. And I can decode it in Python.

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
