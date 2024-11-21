import requests

class ApiClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()  
        return response