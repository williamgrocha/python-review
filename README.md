# Python Review — CRUD com SQLite e API REST

Este projeto foi desenvolvido com o objetivo de revisar e consolidar conceitos fundamentais e intermediários de Python, além de praticar o uso de banco de dados com SQLite e a construção de uma API REST.

Inicialmente, a aplicação utilizava arquivos JSON para persistência de dados, mas posteriormente foi migrado para SQLite, permitindo aplicar conceitos de SQL e simular um cenário mais próximo de aplicações reais.

O projeto evoluiu de um sistema de linha de comando (CLI) para uma API REST utilizando FastAPI, mantendo a separação entre lógica de negócio e acesso a dados.



## 🛠️ Funcionalidades

### Interface via API REST
- Criar nomes ('POST /nomes')
- Listar nomes cadastrados ('GET /nomes')
- Atualizar nomes existentes ('PUT /nomes')
- Remover nomes ('DELETE /nomes/{nome}')

### Persistência
- Armazenamento dos dados em banco SQLite
- Garantia de unicidade de nomes
- Tratamento de erros e validações

## 🧠 Conceitos praticados

- Estruturação de código em múltiplos arquivos (`main.py` e `db.py`)
- Separação de responsabilidades (API e acesso a dados)
- Criação de API REST com FastAPI
- Uso de modelos de dados com Pydantic
INteração com banco de dados SQLite
- Operações SQL básicas:
  - `CREATE TABLE`
  - `INSERT`
  - `SELECT`
  - `UPDATE`
  - `DELETE`
- Validação de entrada e tratamento de erros



## 🧰 Tecnologias utilizadas

- Python 3
- FastAPI
- SQLite3 (via módulo `sqlite3` da biblioteca padrão)
- Pydantic
- Uvicorn

