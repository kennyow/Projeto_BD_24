import MySQLdb



def conectar():
    """
    Função para conectar ao servidor
    """
    #print('Conectando ao servidor...')
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='root',
            passwd='kennyow86!'
        )
        return conn
    except MySQLdb.Error as e:
        print(f"Erro na conexão ao MySQL Server: {e}")

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    #print('Desconectando do servidor...')
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    #
    # print('Listando produtos...')
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
    print('\033[33m ========= PROJETO FARMÁCIA - BANCO DE DADOS - CDIA UFPB ==============\033[m')
    print('Selecione uma opção: ')
    print('1 - Inserir produtos.')
    print('2 - Alterar/Atualizar produtos.')
    print('3 - Pesquisar produtos.')
    print('4 - Deletar produto.')
    print('5 - Listar produto.')
    print('6 - Exibir produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            inserir()
        elif opcao == 2:
            atualizar()
        elif opcao == 3:
            pesquisar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            exibir()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
