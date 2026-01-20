import db
     
def menu():
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Sair")

def cadastrar_nome():
    nome = input("Digite um nome: ")
    nome = nome.strip()
    nome = nome.capitalize()

    if nome == "":
        print("Insira um nome válido.")
        return
    if not db.inserir_nome():
        print("Esse nome já consta em nossos cadastros.")
    else:
        print("Nome cadastrado com sucesso!")

def listar_nomes():
    resultado = db.mostrar_nomes()
    if resultado == []:
        print("Não há nenhum nome na lista.")
    else:
        for i in resultado:
            print(">", i[0])
    
def remover_nome():
    nome = input("Nome a ser removido: ")
    nome = nome.strip()
    nome = nome.capitalize()
    if nome == "":
        print("Nome inválido. Tente novamente.")
        return
    if db.deletar_nome(nome):
        print("%s foi removido com sucesso."%nome)
    else:
        print("Esse nome não consta em nossos registros.")

def main():
    db.init_db()
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

if __name__ == "__main__":
    main()