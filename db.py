import sqlite3

def init_db():
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoas
                (id INTEGER PRIMARY KEY, nome TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

def mostrar_nomes():
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("SELECT nome FROM pessoas")
    resultado = c.fetchall()
    conn.close()
    return resultado

def inserir_nome(nome):
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM pessoas WHERE nome = ?", (nome, ))
    if c.fetchone() is not None:
        conn.close()
        return False
    else:
        c.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome, ))
        conn.commit()
        conn.close()
        return True
    
def deletar_nome(nome):
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    c.execute("DELETE FROM pessoas WHERE nome = ?", (nome,))
    conn.commit()
    if c.rowcount == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True
    
def alterar_nome(nomeAntigo, novoNome):
    conn = sqlite3.connect("nomes.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE pessoas SET nome = ? WHERE nome = ?", (novoNome, nomeAntigo))
        if c.rowcount == 0:
            conn.close()
            return False
        else:
            conn.commit()
            conn.close()
            return True
    except sqlite3.IntegrityError:
        conn.close()
        return 0
