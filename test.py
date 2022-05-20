import requests

response =  requests.get('http://facebook.com')
print(response.status_code)