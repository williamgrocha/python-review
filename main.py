nomes = []

def menu():
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Sair")

def cadastrar_nome():
    nome = input("Digite um nome: ")
    nome = nome.strip()
    nome = nome.capitalize()
    if nome in nomes:
        "Esse nome já foi cadastrado. Tente novamente."
    elif nome == "":
        print("Insira um nome válido.")
    else:
        nomes.append(nome)
        print("Nome cadastrado!")

def listar_nomes():
    if nomes == []:
        print("Não há nenhum nome cadastrado.")
    else:
        print("Nomes cadastrados: ")
        for n in nomes:
            print(">", n)

def remover_nome():
    remover = input("Nome a ser removido: ")
    remover = remover.strip()
    remover = remover.capitalize()
    if remover in nomes:
        nomes.remove(remover)
        print(remover, "foi removido com sucesso!")
    else: 
        print("Este nome não consta na lista.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_nome()
    elif opcao == "2":
        listar_nomes()

    elif opcao == "3":
        remover_nome()

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção Inválida")