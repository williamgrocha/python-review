def menu():
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Sair")

nomes = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite um nome: ")
        nomes.append(nome)
        print("Nome cadastrado!")

    elif opcao == "2":
        print("Nomes cadatrados:")
        for n in nomes:
            print(">", n)

    elif opcao == "3":
        print("Saindo...")
        break
    
    else:
        print("Opção Inválida")