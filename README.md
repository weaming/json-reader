# JSON Reader

Read JSON and it's variants from a char stream.

## Install

```
pip install -U json-reader
```

## Usage

* See `json_reader/test_scanner.py`
* `cat example.log | python -m json_reader`
* `cat example.log | json_reader`

### Environemnts

* `JSON_INDENT`: specify the output indent in integer.
* `BY_LINES`: flag to read stdin line by line, then JSON content must NOT spand cross multiple lines.
