import requests

with requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados") as resposta:
    if resposta.status_code == 200:
        for estado in resposta.json():
            print(30 * "-")
            print("ID:", estado["id"])
            print("Sigla:", estado["sigla"])
            print("Nome:", estado["nome"])
            print("Região:", estado["regiao"]["nome"])
    else:
        print("Erro ao enviar a requisição!")