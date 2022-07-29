import json
import requests

base = "http://127.0.0.1:5000/"

data = [{"likes":78, "name":"zeni", "views":1000},
        {"likes":5,  "name":"mbo",  "views":900},
        {"likes":10, "name":"jeo",  "views":12000}]


#make_request = requests.get(base + "Helloworld/1")
#response = requests.post(base + "Helloworld")

# new_reponse = requests.put(base + "Helloworld/0",{"likes":78,"name":"zeni","views":1000})
# print(new_reponse)


reponse = requests.get(base + "Helloworld/0")
print(reponse.json())