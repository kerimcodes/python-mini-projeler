import requests

url =  "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
veriler = response.json()
gorev_sayilari = {}

for veri in veriler:
    userıd = veri["userId"]
    if userıd in gorev_sayilari:
        gorev_sayilari[userıd] += 1
    else:
        gorev_sayilari[userıd] = 1

for gorev_sayaci in gorev_sayilari:
    print(f"Kullanıcı {gorev_sayaci} : {gorev_sayilari[gorev_sayaci]} görev")