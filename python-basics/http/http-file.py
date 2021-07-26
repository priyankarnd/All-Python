#HTTP requests
import requests

#Making a GET request
#r = requests.get('https://www.google.com')

'''
r.status_code - HTTP status code
r.headers - HTTP headers
r.text - Response text
'''
'''
print(r.status_code)
print(r.headers)

print("\n")
print(r.text)

#Downloading and saving an image
#Python logo

imageData = requests.get("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
with open('logo.png', 'wb') as i:
    i.write(imageData.content)
'''

#passing in arguments (query string parameters) in our get request

#Search Github's repository using a GET request
response = requests.get(
    'https://api.github.com/search/repositories' ,
    params = {'q' : 'requests+language:python'}
)

#Inspect some attributes of the requests repository
json_response = response.json()
print("Result")
repository = json_response['items'][0]
print(f'Repository Name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')





