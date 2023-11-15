import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # data_list = []
        # data = json.loads(self.get_response_body())
        # for item in data:
        #     data_list.append(item("employee"))
            
        # return data_list
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()