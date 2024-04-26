import MySQLdb



def conectar():
    """
    Função para conectar ao servidor
    """
    #print('Conectando ao servidor...')
    try:
        conn = MySQLdb.connect(
            db='farmacia',
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
    qtde = int(input('Selecione quantos itens deseja ver: '))
    cursor.execute(f"SELECT * FROM medicamentos LIMIT {qtde}")
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print("Listando Produtos")
        print("--------------------")
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Produto: {produto[1]}")
            print(f"Categoria: {produto[3]}")
            print(f"Classe Terapêutica: {produto[5]}")
            print(f"Vencimento: {produto[4]}")
            print(f"Valor: R$ {produto[7]}")
            print("--------------------")
    else:
        print("Não existem medicamentos cadastrados")
    desconectar(conn)

def inserir():
    """
    Função para inserir um medicamento
    """  
    #print('Inserindo produto...')
    conn = conectar()
    cursor = conn.cursor()

    print('CADASTRO DO MEDICAMENTO')
    nome = input('Nome do medicamento: ')
    categoria = input('Informe a categoria: ')
    vencimento = input('Informe a data de vencimento (Ex: 21-12-2): ')
    classe = input('Informe a classe terapêutica: ')
    situacao = input('Informe a situação de registro: ')
    principio = input('Informe o principio ativo: ')
    preco = float(input('Informe o preço: '))  

    cursor.execute(f"INSERT INTO medicamentos (id, nome, categoria_regulatoria, data_vencimento_registro, classe_terapeutica, situacao_registro, principio_ativo, preco) VALUES (NULL, '{nome}', '{categoria}', '{vencimento}', '{classe}', '{situacao}', '{principio}', {preco})")
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

    codigo = int(input('Informe o codigo do medicamento que deseja atualizar: '))
    nome = input('Novo Nome do produto: ')
    categoria = input('Informe a categoria: ')
    vencimento = input('Informe a data de vencimento (Ex: 21-12-2): ')
    classe = input('Informe a classe terapêutica: ')
    situacao = input('Informe a situação de registro: ')
    principio = input('Informe o principio ativo: ')
    preco = float(input('Informe o preço: ')) 

    cursor.execute(f"UPDATE medicamentos SET nome='{nome}', categoria_regulatoria='{categoria}', data_vencimento_registro='{vencimento}', classe_terapeutica='{classe}', situacao_registro='{situacao}', principio_ativo='{principio}', preco='{preco}' WHERE id='{codigo}'")

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

    codigo = int(input('Informe o codigo do medicamento: '))
    cursor.execute(f"DELETE FROM medicamentos WHERE id={codigo}")

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi excluido')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')

def pesquisar():
    """
    Função para pesquisar um produto
    """  
    
    conn = conectar()
    cursor = conn.cursor()

    ask = int(input('Deseja realizar a pesquisa pelo (1-nome) ou (2-id): '))

    if ask == 1:
        nome = str(input('Informe o nome do medicamento: '))
        cursor.execute(f"SELECT * FROM medicamentos WHERE nome='{nome}'")
        produto = cursor.fetchone()
        if produto:
            print("--------------------")
            print(f"Nome: {produto[1]}")
            print("--------------------")
            print(f"ID: {produto[0]}")
            print(f"Categoria: {produto[2]}")
            print(f"Vencimento: {produto[3]}")
            print(f"Classe Terapêutica: {produto[4]}")
            print(f"Situação: {produto[5]}")
            print(f"Princípio Ativo: {produto[6]}")
            print(f"Valor: R$ {produto[7]}")
            print("--------------------")
        else:
            print("Medicamento não encontrado")
    elif ask == 2:
        aid = int(input('Informe o id do medicamento: '))
        cursor.execute(f"SELECT * FROM medicamentos WHERE id={aid}")
        produto = cursor.fetchone()
        if produto:
            print("--------------------")
            print(f"ID: {produto[0]}")
            print("--------------------")
            print(f"Nome: {produto[1]}")
            print(f"Categoria: {produto[2]}")
            print(f"Vencimento: {produto[3]}")
            print(f"Classe Terapêutica: {produto[4]}")
            print(f"Situação: {produto[5]}")
            print(f"Princípio Ativo: {produto[6]}")
            print(f"Valor: R$ {produto[7]}")
            print("--------------------")
        else:
            print("Medicamento não encontrado")
    else:
        print("Opção inválida")

    # Verifica se a consulta retornou algum resultado
    results = cursor.fetchall()
    '''if results:
        for row in results:
            print(row)
    else:
        print("Nenhum resultado encontrado.")'''

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi exibido com sucesso')
    else:
        print(f'Produto {nome} não consta na base de dados')

    desconectar(conn)

def exibir():
    """
    Função para exibir relatório
    """  
    
    conn = conectar()
    cursor = conn.cursor()

    print('RELATÓRIO MEDICAMENTOS')
    print('------------------------------------------')

    
    cursor.execute("SELECT COUNT(nome) AS QtdeMed FROM medicamentos;")
    result = cursor.fetchone()
    print("Quantidade de Medicamentos:", result[0])
    print('------------------------------------------')

    print('Quantidade por Categoria Regulatória')
    print('------------------------------------------')
    cursor.execute("SELECT DISTINCT(categoria_regulatoria) AS Categoria, COUNT(categoria_regulatoria) AS Quantidade FROM medicamentos GROUP BY Categoria ORDER BY Quantidade DESC;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('------------------------------------------')
    print('Data do Vencimento perto do dia de hoje (10 mais próximos)')
    print('------------------------------------------')
    cursor.execute("SELECT nome as MEDICAMENTO, data_vencimento_registro AS Data_vencimento, DATEDIFF(curdate(), data_vencimento_registro) AS PRAZO, situacao_registro AS Situação FROM medicamentos WHERE DATEDIFF(curdate(), data_vencimento_registro) < 0 ORDER BY data_vencimento_registro ASC LIMIT 10;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('------------------------------------------')
    print('Quantitativo de Situação de Registro')
    print('------------------------------------------')
    cursor.execute("SELECT DISTINCT(situacao_registro) AS Situação, COUNT(situacao_registro) AS Quantidade FROM medicamentos GROUP BY Situação ORDER BY Quantidade DESC;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('------------------------------------------')
    print('Remédios de menor valor e sua categoria')
    print('------------------------------------------')
    cursor.execute("SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, preco as PREÇO FROM medicamentos WHERE preco = (SELECT MIN(preco) FROM medicamentos) ORDER BY nome;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('------------------------------------------')
    print('Remédios de maior valor e sua categoria')
    print('------------------------------------------')
    cursor.execute("SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, preco as PREÇO FROM medicamentos WHERE preco = (SELECT MAX(preco) FROM medicamentos) ORDER BY nome;")
    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.commit()

    if cursor.rowcount == 1:
        print(f'Relatório Exibido com sucesso')
    else:
        print(f'Erro ao reportar o Relatório')

def exibir_clientes():
    """
    Função para exibir clientes cadastrados
    """  
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes;")

        clientes = cursor.fetchall()

        if len(clientes) > 0:
            print("Listando Clientes")
            print("--------------------")
            for cliente in clientes:
                print(f"ID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Telefone: {cliente[2]}")
                print(f"Endereço: {cliente[3]}")
                print(f"Cidade: {cliente[4]}")
                print(f"IsFlamengo: {cliente[5]}")
                print(f"IsOnePiece: {cliente[6]}")
                print(f"IsSousa: {cliente[7]}")
                print("--------------------")
        else:
            print("Não existem clientes cadastrados")
    except MySQLdb.Error as e:
        print(f"Erro ao acessar a tabela clientes: {e}")
    finally:
        desconectar(conn)

def inserir_cliente():
    """
    Função para inserir um cliente
    """  
    
    conn = conectar()
    cursor = conn.cursor()

    print('CADASTRO DE CLIENTE')
    nome = input('Nome do cliente: ')
    telefone = input('Informe o telefone: ')
    endereço = input('Informe o endereço: ')
    cidade = input('Informe a cidade: ')
    isflamengo = input('Informe se é Flamengo (y/n): ')
    isonepiece = input('Informe se é fã de One Piece(y/n): ')
    issousa = input('Informe se é de Sousa(y/n): ')  


    cursor.execute(f"INSERT INTO clientes (idcliente, nome, telefone, endereco, cidade, isflamengo, isonepiece, issousa) VALUES (NULL, '{nome}', '{telefone}', '{endereço}', '{cidade}', '{isflamengo}', '{isonepiece}', '{issousa}')")
    conn.commit()



def menu():
    """
    Função para gerar o menu inicial
    """
    print()
    print('\033[33m ========= PROJETO FARMÁCIA - BANCO DE DADOS - CDIA UFPB ==============\033[m')
    print('Selecione uma opção: ')
    print('1 - Inserir produtos.')
    print('2 - Alterar/Atualizar produtos.')
    print('3 - Pesquisar produtos.')
    print('4 - Deletar produto.')
    print('5 - Listar produto.')
    print('6 - Exibir relatório.')
    print('7 - Exibir clientes.')
    print('8 - Inserir cliente.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4, 5, 6, 7, 8]:
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
        elif opcao == 7:
            exibir_clientes()
        elif opcao == 8:
            inserir_cliente()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
