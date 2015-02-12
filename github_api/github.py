API_TOKEN='your github token'
GIT_API_URL='https://api.github.com'

import requests


username=raw_input("Enter the Github_User_Name: ")

url='https://api.github.com/users/'+username+'/repos'


url = '%s?access_token=%s' % \
    (url,API_TOKEN,)

r = requests.get(url).json()
for data in r:
	print data["full_name"]
