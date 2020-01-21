import requests

import requests, json

class DirectusClient:

    def __init__(self, url, project, email, password):
        self.url = url
        self.email = email
        self.password = password

        payload = {
            "email": email,
            "password": password
        }

        combined_url = url + '/' + project + '/auth/authenticate'
        r = requests.post(combined_url, data=payload)
  
        # extracting data in json format 
        data = r.json() 

        ACCESS_TOKEN = data['data']["token"]

        print(ACCESS_TOKEN)