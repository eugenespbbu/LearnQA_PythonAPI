import requests
import json
import time

response = requests.request("get","https://playground.learnqa.ru/ajax/api/longtime_job")


string_as_json_format = response.text
json_text = json.loads(string_as_json_format)
token1 = json_text['token']
time1 = json_text['seconds']


response = requests.request("get","https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token1})
string_as_json_format = response.text
json_text = json.loads(string_as_json_format)

if json_text['status'] == 'Job is NOT ready':
    print('Полёт стабильный')
else:
    print('Щеф, всё пропало!!111')


time.sleep(time1+1)
response = requests.request("get","https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token1})
string_as_json_format = response.text
json_text = json.loads(string_as_json_format)

if json_text['status'] == 'Job is ready':
    print('Всё ровно, результат =', json_text['result'])
else:
    print('Шоб я еще сел за баранку этого пылесоса!!!')