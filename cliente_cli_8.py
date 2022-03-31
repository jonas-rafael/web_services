import requests

url_prefixo = "http://localhost:4443"




def criar_sessao():
    s = requests.session()
    return s
def ler():
    nome = str(input("Digite o nome do Contato: "))
    email = str(input("Digite o e-mail do contato: "))
    fone = int(input("Digite a telefone do Contato: "))
    data_nasc = (input("Digite a data de nascimento do contato (aaaa-mm-dd): "))

    return {
        "nome": nome,
        "email": email,
        "fone": fone,
        "data_nasc": data_nasc
    }

def imprimir(contato):
    print("#")
    print("ID:", contato["id"])
    print("Nome:", contato["nome"])
    print("E-mail:", contato["email"])
    print("Telefone:", contato["fone"])
    print("Data de Nascimento:", contato["data_nasc"])