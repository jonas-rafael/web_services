import requests

codigo = int(input("Digite o código do estado: "))

with requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo}/municipios") as resposta:
    if resposta.status_code == 200:
        for municipios in resposta.json():
            print(30 * "-")
            print("Nome:", municipios["nome"])
            print("Microrregião:", municipios["microrregiao"]["nome"])
            print("Mesorregião:", municipios["microrregiao"]["mesorregiao"]["nome"])
    else:
        print("Erro ao enviar a requisição!")