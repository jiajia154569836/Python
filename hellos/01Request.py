import requests
import json
r = requests.get('http://httpbin.org/get')
print(r.url)


payload = {
    'key1': 'value1',
    'key2': 'value2'
}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

headers = {
      'hello': 'world'
}
r = requests.get('http://httpbin.org/get', headers=headers)
print(r.text)

payload = {
        'hello': 'world'
}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
print(r.text)