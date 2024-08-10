import requests
url="https://api.github.com/user"
h={"Authorization": "Bearer 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" }
respuesta=requests.get(url=url,headers=h)
print (respuesta.json())