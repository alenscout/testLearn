import requests

request1 = requests.get("https://github.com/alenscout/testLearn/new/master")
print(request1.status_code)
print("hiiii")