import requests

request1 = requests.get("https://github.com/alenscout/testLearn/new/master")
print(request1.status_code)
print("hiiii")
albania = [1,2,3,4,5]
greece = "1,2,3,4,5"

def func(rebz):
    if rebz != 0:
        return rebz
    else:
        return "error"
print(func(0))