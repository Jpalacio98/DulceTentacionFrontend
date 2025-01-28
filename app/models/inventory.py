import requests, os


class Inventory():
    def __init__(self):
        super().__init__()
        self.data ={}
        self.headers = {"Content-Type": "application/json"}
        self.url = os.getenv("BackendUrl")

    def add(self, data):
        url = self.url+"/register_product"
        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 201:
            print("Recurso creado!")
            print(response.json())
            return True
        else:
            print(f"Error: {response.status_code}")
            return False

