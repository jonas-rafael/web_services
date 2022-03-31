import requests
#definir região correta pra printar

try:
    cep=int(input("Digite o cep: "))
except (ValueError, NameError):
    print("cep no formato incorreto, tente novamente!")


def municipio(muni):
    with requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{muni}/municipios") as resposta1:
        if resposta1.status_code == 200:
            for municipio in resposta1.json():
                if municipio["nome"] == "São Gonçalo do Amarante":
                    print(30 * "-")
                    print("Nome:", municipio["nome"])
                    print("Microrregião:", municipio["microrregiao"]["nome"])
                    print("Mesorregião:", municipio["microrregiao"]["mesorregiao"]["nome"])
try:
    with requests.get(f"https://viacep.com.br/ws/{cep}/json/")as resposta:

        if resposta.status_code == 200:
            j= resposta.json()
            print("rua: ", j["logradouro"])
            print("Bairro: ", j["bairro"])
            print("Cidade: ", j["localidade"])
            print("Estado:", j["uf"])
            muni=j["uf"]
            imprimir=municipio(muni)
            print(imprimir)
        else:
            print("Cep não encontrado, tente novamente!")

except (ValueError,NameError):
    print(" ")