import requests

link = 'https://jsonplaceholder.typicode.com/posts'
response = requests.post(link, data={

    'userId': 12,
    'title': 'My new post',
    'body': 'body for new post'
})

print(requests.get(link).text)
print('\nAdding data\n')
print(response.text)
