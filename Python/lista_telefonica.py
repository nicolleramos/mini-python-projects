import copy

# Variável global para armazenar o ID inicial e a lista de contatos
id_global = 5018397
lista_contatos = []

# Contato inicial para testar a aplicação
estudante = {
  "id": id_global,
  "nome": "nicolle",
  "atividade": "estagiária",
  "telefone": "0325****"
}
lista_contatos.append(estudante)

# Função principal que exibe o menu principal e navega pelas opções do programa
def exibir_menu_principal():
    global id_global
    while True:
        # Exibição do menu principal
        print("\n ***************************************")
        print("*****************************************")
        print(r"""
   ,==.-------.
  (    ) ====  \
  ||  | [][][] |  bem-vindo à lista telefônica 
,8||  | [][][] |    da Nicolle Ramos Batista!
8 ||  | [][][] |
8 (    ) O O O /
'88`=='-------' 
  """)
        print("#### MENU #### \n")
        print(" ***************************************")
        print("|*| Como posso te ajudar?")
        print("    [1] Adicionar um novo contato")
        print("    [2] Consultar contatos(s)")
        print("    [3] Remover um contato")
        print("    [4] Sair")
        print("*****************************************")

        # Solicita a opção do usuário e faz o tratamento de erro caso a entrada seja inválida
        try:
            opcao = int(input(":: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Lógica para navegar pelas opções do menu
        if opcao == 1:
            id_global += 1
            cadastrar_novo_contato(id_global)  # Chama a função para adicionar um contato
        elif opcao == 2:
            consultar_contatos()  # Chama a função para consultar contatos
        elif opcao == 3:
            excluir_contato()  # Chama a função para remover um contato
        elif opcao == 4:
            break  # Sai do programa
        else:
            print("Opção inválida! Tente novamente.")

# Função responsável por adicionar um novo contato à lista de contatos
def cadastrar_novo_contato(id):
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Adicionar um novo contato")
    print("---------------------------------------")
    print("id deste contato:", id)

    # Coleta as informações do contato do usuário
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    # Cria o dicionário com os dados do novo contato
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    # Utiliza a função copy para copiar o dicionário e adicionar à lista de contatos
    novo_contato = copy.copy(contato)
    lista_contatos.append(novo_contato)
    print("Contato adicionado com sucesso! \n")

# Função responsável por consultar contatos com base em diferentes critérios
def consultar_contatos():
    while True:
        # Exibe o menu de consulta
        print("____________________________________")
        print("\n## MENU Consultar contatos ##")
        print("\n|*| Como deseja consultar?")
        print("    [1] Consultar todos os contatos")
        print("    [2] Consultar contato(s) por id")
        print("    [3] Consultar contato(s) por atividade")
        print("    [4] Voltar ao menu principal")
        print("------------------------------------")

        # Solicita a opção de consulta do usuário
        try:
            opcao = int(input(":: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Consultar todos os contatos
        if opcao == 1:
            if lista_contatos:
                # Exibe todos os contatos cadastrados
                for contato in lista_contatos:
                    print("\n* id: ", contato["id"])
                    print("  | nome:", contato["nome"])
                    print("  | atividade:", contato["atividade"])
                    print("  | telefone:", contato["telefone"], "\n")
            else:
                print("Não há contatos cadastrados!")

        # Consultar contato por ID
        elif opcao == 2:
            try:
                id_consulta = int(input("|*| Digite o id do contato que deseja buscar: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            # Busca o contato pelo ID fornecido
            encontrado = False
            for contato in lista_contatos:
                if (contato["id"] == id_consulta):
                    encontrado = True
                    print("* id:", contato["id"])
                    print("  | nome:", contato["nome"])
                    print("  | atividade:", contato["atividade"])
                    print("  | telefone:", contato["telefone"], "\n")
                    break
            if not encontrado:
                print("Contato não encontrado!")

        # Consultar contato por atividade
        elif opcao == 3:
            atividade_consulta = input("|*| Digite a atividade do contato que deseja buscar: ").lower()

            # Busca o contato pela atividade fornecida
            encontrado = False
            for contato in lista_contatos:
                if (contato["atividade"].lower() == atividade_consulta):
                    encontrado = True
                    print("* id:", contato["id"])
                    print("  | nome:", contato["nome"])
                    print("  | atividade:", contato["atividade"])
                    print("  | telefone:", contato["telefone"], "\n")
            if not encontrado:
                print("Nenhum contato encontrado com essa atividade!")

        # Volta ao menu principal
        elif opcao == 4:
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função responsável por remover um contato da lista de contatos
def excluir_contato():
    try:
        remover_id = int(input("|*| Digite o id do contato que deseja remover: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    # Busca o contato pelo ID fornecido e remove da lista
    encontrado = False
    for contato in lista_contatos:
        if (contato["id"] == remover_id):
            encontrado = True
            lista_contatos.remove(contato)
            print("Contato removido com sucesso! \n")
            break
    if not encontrado:
        print("Contato não encontrado!")

# Ponto de entrada do programa
if __name__ == "__main__":
    exibir_menu_principal()  # Chama a função principal que exibe o menu
