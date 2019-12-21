PLAIN_JSON = '''{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  + verbose: true
  - proxy: 123.234.53.22
}'''

PLAIN_YAML = '''{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  + verbose: true
  - proxy: 123.234.53.22
}'''

COMPLEX_JSON = '''{
    common: {
        setting1: Value 1
        setting3: true
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

PLAIN_FORMAT = '''Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting2' was removed
Property 'common.setting6' was removed
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'group3' was added with value: 'complex value'
Property 'group2' was removed'''


JSON_FORMAT = '''{\
"common": {"type": "children", "value": {\
"setting1": {"type": " ", "value": "Value 1"}, \
"setting3": {"type": " ", "value": true}, \
"setting4": {"type": "+", "value": "blah blah"}, \
"setting5": {"type": "+", "value": {"key5": "value5"}}, \
"setting2": {"type": "-", "value": "200"}, \
"setting6": {"type": "-", "value": {"key": "value"}}}}, \
"group1": {"type": "children", "value": {\
"baz": {"type": "changed", "old_value": \
"bas", "new_value": "bars"}, \
"foo": {"type": " ", "value": "bar"}}}, \
"group3": {"type": "+", "value": {"fee": "100500"}}, \
"group2": {"type": "-", "value": {"abc": "12345"}}}'''
