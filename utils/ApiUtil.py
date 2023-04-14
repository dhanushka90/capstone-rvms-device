import json

import requests


class ApiUtil:

    def post_req(self, api_url, data):
        print("Calling API", api_url)
        response = requests.post(api_url, data=json.dumps(data), headers= {'Content-Type': 'application/json'})
        print("response status: ", response.status_code)

        return response.json()

    def get_req(self, api_url):
        print("Calling get api: ", api_url)
        response = requests.get(api_url)
        print("response status: ", response.status_code)

        return response.json()
