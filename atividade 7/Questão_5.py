import requests

sigla=str(input("Digite a sigla do estado desejado: ").upper())

with requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios") as resposta:

    if resposta.status_code == 200:
        con=None
        for j in resposta.json():
            print(30*"*_")
            print("Nome: ", j["nome"])
            print("Microrregião: ",j["microrregiao"])
            print("Mesorregião: ",j["microrregiao"]["mesorregiao"])

    else:
        print("Sigla do estado não encontrada!")



