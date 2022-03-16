import requests


palavra=str(input("Digite a palavra para busca"))




with requests.get(f"https://api.dicionario-aberto.net/word/{palavra}/1") as resposta:
    if resposta.status_code == 200:
        con=resposta.json()
        for j in resposta.json():
            print(j)
            print(20*"*")
            print("palavra", j["word"])
            print(20*"*")
            print("descrição", j["xml"])

        if con == ([ ]):
             print(30 * "*")
             print("Palavra Digitada não encontrada\nVeja essas palavras semelhantes, e tente novamente!")
             print(30*"*")
             with requests.get(f"https://api.dicionario-aberto.net/near/{palavra}") as resposta:
                 print(resposta.json())
                 print(30*"*")













