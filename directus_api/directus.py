import requests, json

class DirectusClient:

    def __init__(self, url, project, email=None, password=None):
        self.url = url + '/' + project
        self.email = email
        self.password = password
        self.project = project
        self.access = None

        if email is not None and password is not None:

            payload = {
                "email": email,
                "password": password
            }

            combined_url = self.url + '/auth/authenticate'
            r = requests.post(combined_url, data=payload)
            data = r.json() 

            self.access = data['data']["token"]

    def get_items_list(self, collection):
        return requests.get(self.url + "/items/" + collection).json()

    def get_item(self, collection, id):
        return requests.get(self.url + "/items/" + collection + "/" + str(id)).json()

    def create_item(self, collection, item):
        return requests.post(self.url + "/items/" + collection, data=item)

    def get_files_list(self):
        headers = {"Authorization": "Bearer " + self.access}
        return requests.get(self.url + "/files", headers=headers).json() 

    def get_file(self, id):
        headers = {"Authorization": "Bearer " + self.access}
        return requests.get(self.url + "/files/" + str(id), headers=headers).json()
