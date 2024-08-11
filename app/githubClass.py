import requests
class GithubClient:
    
    def __init__(self) -> None:
        self.baseUrl="https://api.github.com"
        self.token="cambiaaquiportutoken"
    
    def queryUser(self):
        h={"Authorization": "Bearer {}".format(self.token) }
        url=self.baseUrl+"/user"
        resp=requests.get(url=url,headers=h)
        return resp.json()
    

        