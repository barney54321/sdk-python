import requests

import requests, json

class DirectusClient:

    def __init__(self, url, project, email, password):
        self.url = url + '/' + project
        self.email = email
        self.password = password
        self.project = project

        payload = {
            "email": email,
            "password": password
        }

        combined_url = self.url + '/auth/authenticate'
        r = requests.post(combined_url, data=payload)
  
        # extracting data in json format 
        data = r.json() 

        ACCESS_TOKEN = data['data']["token"]

    def get_items(self, collection, id=None):
        # GET /:project/items/:collection

        if id is None:
            return requests.get(self.url + "/items/" + collection).json()
        else:
            return requests.get(self.url + "/items/" + collection + "/" + str(id)).json()