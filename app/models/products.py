import requests, os


class Menu():
    def __init__(self):
        super().__init__()
        self.data ={}
        self.headers = {"Content-Type": "application/json"}
        self.url = os.getenv("BackendUrl")+"/menu"

    def add(self, data):
        url = self.url+"/add"
        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 201:
            print("Recurso creado!")
            print(response.json())
            return True
        else:
            print(f"Error: {response.status_code}")
            return False
    
    def list(self):
        url = self.url+"/list"
        response = requests.get(url)

        if response.status_code == 200:
            #print(response.json())
            return True,response.json()
        else:
            #print(f"Error: {response.status_code}")
            return False, f"Error: {response.status_code}"

