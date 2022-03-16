import requests
name=str(input("Digite o nome do país: "))

def lugar(país):
    with requests.get(f"http://universities.hipolabs.com/search?name=&country={país}")as universidades:
        if universidades.status_code == 200:
            for j in universidades.json():
                print(20*"*")
                print("País:", j["country"])
                print("Nome: ", j ["name"])
                print("site:", j["domains"])

controle=None
with requests.get(f"https://restcountries.com/v3.1/name/{name}")as resposta:
    if resposta.status_code == 200:
        con = resposta.json()
        for j in resposta.json():

            print("país: ", j["name"]["common"])
            país=j["name"]["common"]
            print(lugar(país))

        if con == [ ]:
            print("entrada inválida")