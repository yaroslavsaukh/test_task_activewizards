import requests

link = 'https://httpbin.org/post'

data = {'hello': 'world', 'world': 'hello'}
response = requests.post(link, data=data)
print(response.text)
