from getpass import getpass
import requests


def ler_login():
    matricula = input("Digite sua matricula: ")
    senha = getpass("Digite a sua senha: ")

    return {"username": matricula, "password": senha}
def criar_session(login):
    s = requests.Session()

    with s.post("https://suap.ifrn.edu.br/api/v2/autenticacao/token/",data=login)as resposta:
        dados =resposta.json()
        if resposta.status_code == 200:
            s.headers["Authorization"] = f"JWT {dados['token']}"
        else:
            print("Código do erro:", resposta.status_code)
            print("Mensagem do erro:", dados["detail"])
            s = None


def main():
    sessao = criar_session(ler_login())
    anoletivo=int(input("Digite o ano letivo"))
    periodo=int(input("Digite a período letivo: "))

    with sessao.get(f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{anoletivo}/{periodo}") as resposta:
        if resposta.status_code == 200:
            dados = resposta.json()

            print("\nMatrícula:", dados["matricula"])
            print("Nome:", dados["nome_usual"])
            print("E-Mail:", dados["email"])
            print("Campus:", dados["vinculo"]["campus"])
            print("Categoria:", dados["vinculo"]["categoria"])
        else:
            print("Erro ao realizar requisição:", resposta.status_code)


if __name__ == "__main__":
    main()