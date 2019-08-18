example1 = """
{
  "a": 3,
  "b": 3.14,
  "c": {
    "d": [
      "x",
      "hello",
      3.14,
      4,
      true,
      false
    ],
    "key": {
      "key words": {
        "g": "abc"
      }
    }
  },
  "aa": NaN,
  "bb": Infinity,
  "cc": -Infinity
}
""".strip()
example2 = example1 + "extra text 1234 {} []"

example3 = """
{
  "a": 3,
  "b": 3.14,
  "c": {
    "d": [
      "x",
      "hello",
      3.14,
      4,
      True,
      False
    ],
    "key": {
      "key words": {
        "g": "abc"
      }
    }
  },
  "aa": nan,
  "bb": infinity,
  "cc": -infinity,
  "dd": "string1"
}
""".strip()
example4 = example3 + "extra text 1234 {} []"


def test_scanner_standard():
    from json_reader.decoder import JSONDecoder

    decoder = JSONDecoder()
    data, index = decoder.raw_decode(example2)
    print(data, example2[index:])


def test_scanner_changed():
    from json_reader.decoder import JSONDecoder
    from json_reader.decoder_case_insensitive import CaseInsensitiveScanner

    decoder = JSONDecoder(scanner_cls=CaseInsensitiveScanner)
    data, index = decoder.raw_decode(example4)
    print(data, example4[index:])
