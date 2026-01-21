import db
     
def menu():
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Atualizar nome")
    print("5 - Sair")

def cadastrar_nome():
    nome = input("Digite um nome: ").strip().capitalize()
    if nome == "":
        print("Insira um nome válido.")
        return
    if not db.inserir_nome(nome):
        print("Esse nome já consta em nossos cadastros. Nada foi alterado.")
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
    nome = input("Nome a ser removido: ").strip().capitalize()
    if nome == "":
        print("Nome inválido. Tente novamente.")
        return
    if db.deletar_nome(nome):
        print("%s foi removido com sucesso."%nome)
    else:
        print("Esse nome não consta em nossos registros. Nada foi alterado.")

def atualizar_nome():
    nome = input("Nome a ser alterado: ").strip().capitalize()
    if nome == "":
        print("Insira um nome válido.")
        return
    novoNome = input("Novo nome: ").strip().capitalize()
    if novoNome == "":
        print("Insira um nome válido.")
        return

    resultado = db.alterar_nome(nome, novoNome)
    if resultado == 0:
        print("O novo nome já consta em nossos registros. Nada foi alterado.")
    elif resultado:
        print("Nome atualizado com sucesso!")
    else:
        print("O nome a ser alterado não consta em nossos registros. Nada foi alterado.")


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
            atualizar_nome()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()