import json, sqlite3

def init_db():
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoas
                (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)''')
    conn.commit()
    conn.close()
     
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
    
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM pessoas WHERE nome = ?", (nome, ))
    if c.fetchone() is not None:
        print("Esse nome já foi cadastrado")
        conn.close()
    else:
        c.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome, ))
        print("Nome cadastrado!")
        conn.commit()
        conn.close()

def listar_nomes():
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("SELECT nome FROM pessoas")
    resultado = c.fetchall()
    conn.close()
    if resultado == []:
        print("Não há nenhum nome na lista.")
    else:
        for i in resultado:
            print(">", i[0])
    
def remover_nome():
    nome = input("Nome a ser removido: ")
    nome = nome.strip()
    nome = nome.capitalize()

    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("DELETE FROM pessoas WHERE nome = ?", (nome,))
    conn.commit()
    if c.rowcount == 0:
        print("Esse nome não consta em nossos cadastros.")
    else:
        print("O nome foi %s removido com sucesso." %nome)
    conn.close()

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