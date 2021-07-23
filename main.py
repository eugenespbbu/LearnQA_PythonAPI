import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

for i in range(10):
    print(response.history[i])
    num_response = response.history[i]
    print(num_response.url)