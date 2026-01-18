import json, sqlite3

def init_db():
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoas
                (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def carregar_dados():
    try:
        with open("lista-nomes.json", "r") as f:
            lista_nomes = f.read()
            x = json.loads(lista_nomes)
            return x
    except FileNotFoundError:
        return []

     
nomes = carregar_dados()
     
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
        print("Esse nome já foi cadastrado. Tente novamente.")
    elif nome == "":
        print("Insira um nome válido.")
    else:
        nomes.append(nome)
        print("Nome cadastrado!")

def listar_nomes():
    if not nomes:
        print("Não há nenhum nome cadastrado.")
    else:
        print("Nomes cadastrados: ")
        for n in nomes:
            print(">", n)

def remover_nome():
    remover = input("Nome a ser removido: ")
    remover = remover.strip()
    remover = remover.capitalize()
    if not nomes:
        print("Não há nenhum nome cadastrado")
    elif remover in nomes:
        nomes.remove(remover)
        print(remover, "foi removido com sucesso!")
    else: 
        print("Este nome não consta na lista.")

def salvar_dados():
    with open('lista-nomes.json', 'w') as f:
        json.dump(nomes, f)

def main():
    init_db()
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
            salvar_dados()
            break

        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()