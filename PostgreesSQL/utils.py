import psycopg2

def conectar():
    """
    Função para conectar ao servidor
    """
    #print('Conectando ao servidor...')
    try:    
        conn = psycopg2.connect(
            database='ppostgresql',
            host='localhost',
            user='kennyow86',
            password='xxxxx'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro na conexão ao PostgreSQL Server: {e}")


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    print('Desconectando do servidor...')
    if conn:
        conn.close()

def listar():
    """
    Função para listar os produtos
    """
    #print('Listando produtos...')
    conn =  conectar()
    cursor  = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print("Listando Produtos")
        print("--------------------")
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Produto: {produto[1]}")
            print(f"Preço: {produto[2]}")
            print(f"Estoque: {produto[3]}")
            print("--------------------")
    else:
        print("Não existem produtos cadastrados")
    desconectar(conn)

def inserir():
    """
    Função para inserir um produto
    """  
    #print('Inserindo produto...')
    conn =  conectar()
    cursor  = conn.cursor()

    nome = input('Nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido')
    else:
        print(f'Não foi possivel inserir')

    desconectar(conn)
def atualizar():
    """
    Função para atualizar um produto
    """
    #print('Atualizando produto...')
    conn =  conectar()
    cursor  = conn.cursor()

    codigo = int(input('Informe o codigo do produto: '))
    nome = input('Novo Nome do produto: ')
    preco = float(input(' Novo  - Informe o preço do produto: '))
    estoque = int(input('Novo - Informe a quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado')
    else:
        print(f'Não foi possivel atualizar')

    desconectar(conn)

def deletar():
    """
    Função para deletar um produto
    """  
    #print('Deletando produto...')
    conn =  conectar()
    cursor  = conn.cursor()

    codigo = int(input('Informe o codigo do produto: '))
    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi excluido')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')

    desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
