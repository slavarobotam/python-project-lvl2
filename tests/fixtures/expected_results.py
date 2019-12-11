PLAIN_JSON = '''{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  + verbose: True
  - proxy: 123.234.53.22
}'''

PLAIN_YAML = '''{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  + verbose: True
  - proxy: 123.234.53.22
}'''

COMPLEX_JSON = '''{
    common: {
        setting1: Value 1
        setting3: True
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
      - setting2: 200
      - setting6: {
            key: value
        }
    }
    group1: {
      + baz: bars
      - baz: bas
        foo: bar
    }
  + group3: {
        fee: 100500
    }
  - group2: {
        abc: 12345
    }
}'''