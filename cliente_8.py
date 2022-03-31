import requests
import cliente_cli_8



def main():

    sessão = cliente_cli_8.criar_sessao()


    while True:
        print("*"*40)
        print(" 0 - Sair do programa")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Atualizar aluno")
        print("4 - Listar contatos")
        print("5 - buscar contatos")
        opção= int(input("Escolha sua opção: "))

        if opção == 0:
            print("Saindo do programa...")
            break
        elif opção == 1:

            with sessão.post(cliente_cli_8.url_prefixo + "/contato", json=cliente_cli_8.ler()) as resposta:
                if resposta.status_code == 201:
                    print("Contato adicionado com sucesso! ")
                else:
                    print("Não foi possivel adicionar o contato", resposta.status_code)
        elif opção == 2:
            email = str(input("Digite o e-mail do contato que deseja remover: "))

            with sessão.delete(cliente_cli_8.url_prefixo + f"/contato/{email}") as resposta:
                if resposta.status_code == 200:
                    print("Contato remvido com sucesso!")
                else:
                    print("Não foi possivel remover contato", resposta.status_code)


        elif opção == 3:
            id=(input("Digite o ID do contato que deseja atualizar: "))
            n_nome=input("Digite o novo nome")
            n_email=str(input("Digite o novo e-mail do contato: "))
            n_fone=int(input("Digite o novo telefone do contato: "))
            n_data_nasc=(input("Digite a nova data de nanscimento do contato aaaa-mm-dd: "))


            dados = {

                "id":id,
                "n_nome":n_nome,
                "n_email":n_email,
                "n_fone":n_fone,
                "n_data_nasc":n_data_nasc
            }

            with sessão.patch(cliente_cli_8.url_prefixo + "/contato", json=dados) as resposta:
                if resposta.status_code == 200:
                    print("Contato atualizado com sucesso!")
                else:
                    print("Não foi possivel atualizar o contato:", resposta.status_code)


        elif opção == 4 :
            with sessão.get(cliente_cli_8.url_prefixo+ "/contato") as resposta:
                if resposta.status_code == 200:
                    for contato in resposta.json():
                        cliente_cli_8.imprimir(contato)
                else:
                    print("Nenhum contato cadastrado: ", resposta.status_code)

        elif opção == 5:
            nome = (input("Digite o nome do contato: "))

            with sessão.get(cliente_cli_8.url_prefixo + f"/contato/{nome}") as resposta:
                if resposta.status_code == 200:
                    for x in resposta.json():
                        cliente_cli_8.imprimir(resposta.json())
                else:
                    print("Nome não encontrado:", resposta.status_code)



if __name__ == "__main__":
    main()