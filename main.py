import requests

method = input()
response = requests.request(method,"https://playground.learnqa.ru/ajax/api/compare_query_type", data={"param1":"method1"})
print(response.status_code)
print(response.text)
print('method =', method)