import requests

request = requests.get("https://github.com/alenscout/testLearn/new/master")
print(request.status_code)