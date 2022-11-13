import requests

url = 'https://api.divar.ir/v8/web-search/1/drink-maker'

json = {"json_schema": {"category": {"value": "drink-maker"}, "query": "قهوه ساز", "cities": ["1"]},
        "last-post-date": 1667559825817700}

headers = {"Content-Type": "applications/json"}

res = requests.post(url, json=json, headers=headers)
data = res.json()
last_post_date = data['last_post_date']
list_of_tokens = []
cont = 0
while True:
    json = {'json_schema': {'category': {'value': "ROOT"}, 'cities': ["1"]}, 'last-post-date': last_post_date}
    res = requests.post(url, json=json, headers=headers)
    data = res.json()
    last_post_date = data['last_post_date']

    for widget in data['web_widgets']['post_list']:
        token = widget['data']['token']
        list_of_tokens.append(token)
        cont += 1
    if cont >= 100:
        break
txt_file = open('tokens.txt', 'w', encoding='utf8')
txt_file.write(','.join(list_of_tokens))
txt_file.close()
