# Python Review — CRUD com SQLite

Este projeto foi criado com o objetivo de revisar e consolidar conceitos fundamentais e intermediários de Python, além de praticar o uso de banco de dados com SQLite.

Inicialmente, o sistema utilizava arquivos JSON para persistência de dados, mas posteriormente foi migrado para SQLite, permitindo aplicar conceitos de SQL e simular um cenário mais próximo de aplicações reais.

O projeto consiste em um sistema simples de CRUD (Create, Read, Update e Delete) para gerenciamento de nomes através de um menu no terminal.

## 🛠️ Funcionalidades

- Cadastrar nomes no banco de dados
- Listar todos os nomes cadastrados
- Remover nomes existentes
- Alterar nomes existentes
- Persistência de dados usando SQLite

## 🧠 Conceitos praticados

- Estruturação de código em múltiplos arquivos (`main.py` e `db.py`)
- Separação de responsabilidades (lógica de interface vs acesso a dados)
- Uso do módulo `sqlite3`
- Operações SQL básicas:
  - `CREATE TABLE`
  - `INSERT`
  - `SELECT`
  - `DELETE`
- Tratamento de erros e validação de entrada do usuário

## 🧰 Tecnologias utilizadas

- Python 3
- SQLite3 (via módulo `sqlite3` da biblioteca padrão)

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone <https://github.com/williamgrocha/python-review.git>

