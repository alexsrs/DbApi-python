import sqlite3
from pathlib import Path

# Definindo o diretório onde colocamos o BD
ROOT_PATH = Path(__file__).parent

# Conexão com o BD
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# Criação da Tabela
def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(155), email VARCHAR(155))")
    conexao.commit()

#inserindo dados
def inserir_registro(conexao, cursor, nome, email): 
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    try:
        cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    except Exception as exc:
        print(f'Ops ! um erro ocorreu! {exc}')
        conexao.rollback()
    finally:
        conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    try:
        cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    except Exception as exc:
        print(f'Ops ! um erro ocorreu! {exc}')
        conexao.rollback()
    finally:
        conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    try:
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    except Exception as exc:
        print(f'Ops ! um erro ocorreu! {exc}')
        conexao.rollback()
    finally:
        conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome;")
    return cursor.fetchall()


cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
print(f'Seja bem vindo ao sistema cliente {cliente["nome"]}')
print()

lista = listar_clientes(cursor)
for item in lista:
    print(dict(item))



#dados = [
#   ("Tito mendes", "lula@zone.uol"),
#   ("Carol louca", "carol@para.br"),
#   ("jessica matoso", "jematos@gmail.com")
#    ]
#inserir_muitos(conexao, cursor, dados)


# atualizar_registro(conexao, cursor, "Joselito atual", "joselito@besta.com", 3)
#inserir_registro(conexao, cursor, "Joselito Barnabe", "chup@rola.cu")
#excluir_registro(conexao, cursor, 5)
#excluir_registro(conexao, cursor, 6)

