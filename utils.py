import MySQLdb
import datetime


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
    mari = input('Informe se é de Mari [S/N]: ').upper()
    situacao = input('Informe a situação de registro: ')
    principio = input('Informe o principio ativo: ')
    estoque = int(input('Informe o estoque: '))
    preco = float(input('Informe o preço: '))  

    cursor.execute(f"INSERT INTO medicamentos (id, nome, categoria_regulatoria, data_vencimento_registro, classe_terapeutica, mari, situacao_registro, principio_ativo, estoque, preco) VALUES (NULL, '{nome}', '{categoria}', '{vencimento}', '{classe}', '{mari}', '{situacao}', '{principio}', '{estoque}',{preco})")
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
    situacao = input('Informe se é de Mari [S/N]: ').upper()
    situacao = input('Informe a situação de registro: ')
    principio = input('Informe o principio ativo: ')
    estoque = int(input('Informe o estoque: '))
    preco = float(input('Informe o preço: ')) 

   
    cursor.execute(f"UPDATE medicamentos SET nome='{nome}', categoria_regulatoria='{categoria}', data_vencimento_registro='{vencimento}', classe_terapeutica='{classe}', situacao_registro='{situacao}', principio_ativo='{principio}', estoque='{estoque}', preco={preco} WHERE id='{codigo}'")


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
            print(f"Situação: {produto[6]}")
            print(f"Princípio Ativo: {produto[7]}")
            print(f"Estoque: {produto[8]} Unidades")
            print(f"Valor: R$ {produto[9]}")
            print("--------------------")
        else:
            print("Medicamento não encontrado")
        return produto
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
            print(f"Situação: {produto[6]}")
            print(f"Princípio Ativo: {produto[7]}")
            print(f"Estoque: {produto[8]} Unidades")
            print(f"Valor: R$ {produto[9]}")
            print("--------------------")
        else:
            print("Medicamento não encontrado")
        return produto
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
                print(f"Email: {cliente[3]}")
                print(f"IsFlamengo: {cliente[4]}")
                print(f"IsOnePiece: {cliente[5]}")
                print(f"IsSousa: {cliente[6]}")
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
    telefone = input('Informe o telef# Obtenha o resultado da consultaone: ')
    email = input('Informe o email do usuário: ')
    isflamengo = input('Informe se é Flamengo (y/n): ')
    isonepiece = input('Informe se é fã de One Piece(y/n): ')
    issousa = input('Informe se é de Sousa(y/n): ') 
    usuario = input('Informe o Usuário para Login: ') 
    senha = input('Informe a Senha para Login: ') 

    cursor.execute(f"INSERT INTO clientes (idcliente, nome, telefone, email, isflamengo, isonepiece, issousa, usuario, senha) VALUES (NULL, '{nome}', '{telefone}', '{email}', '{isflamengo}', '{isonepiece}', '{issousa}', '{usuario}', '{senha}' )")
    conn.commit()

def comprar_produtos():
    """
    Função para comprar medicamentos
    """  
    
    conn = conectar()
    cursor = conn.cursor()
    
    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime('%Y-%m-%d')

    login = input('Login: ')
    senha = input('Senha: ')


    cursor.execute("SELECT idcliente FROM clientes WHERE usuario = %s AND senha = %s", (login, senha))
    resultado = cursor.fetchone()
    if resultado:
        id_usuario = resultado[0]
        print(f'ID DO USUÁRIO: {id_usuario}')
        print("Login efetuado com sucesso!")

        #VENDEDORES
        cursor.execute("SELECT * FROM vendedores_nomes")
        vendedores = cursor.fetchall()

        if len(vendedores) > 0:
            print("Listando Vendedores")
            print("--------------------")
            for vendedor in vendedores:
                print(f"ID: {vendedor[0]} || Nome: {vendedor[1]}")
                print("--------------------")
        
        vendedor = int(input("Selecione o vendedor que o atendeu: "))

        # Inserir dados na tabela compras
        cursor.execute("INSERT INTO compras (idcliente, idvendedor, data_compra, valor_total, forma_pagamento, status_pagamento) VALUES (%s, %s, %s, '0', '1', 'pendente')", (vendedor, id_usuario, data_formatada))

        # Confirmar a transação no banco de dados
        conn.commit()


        fim = ''
        while fim != 'N':
            med = pesquisar()
            qtde = int(input('Quantas unidades deseja adquirir? '))
            nome_item = med[1]
            valor = float(med[-1])
            print(f'Valor total parcial: {valor}')

            cursor.execute(f"SELECT idcompra FROM compras WHERE idcliente = '{id_usuario}' AND idvendedor = '{vendedor}';")

            cursor.execute("SELECT MAX(idcompra) AS ultimo_id FROM compras")
            id_da_compra = cursor.fetchone()  # Ajuste aqui para usar fetchone() em vez de fetchall()
            
            
            if id_da_compra:  # Verifica se a consulta retornou algum resultado
                id_da_compra = id_da_compra[0]  # Acessa o primeiro valor da tupla retornada
                
                # Inserir os dados na tabela itens_compra
                cursor.execute("INSERT INTO itens_compra (iditem, idcompra, nome_item, quantidade, preco_unitario) VALUES (NULL, %s, %s, %s, %s)", (id_da_compra, nome_item, qtde, valor))
                print("Item inserido com sucesso!")

            else:
                print("Nenhuma compra encontrada para o cliente e vendedor especificados.")

            fim = str(input('Deseja realizar outra compra? [S/N]: ')).upper()
            
        # Confirmar a transação no banco de dados
        conn.commit()



        # Executar a consulta SQL
        cursor.execute("SELECT MAX(idcompra) AS ultimo_id FROM compras")

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Verificar se há resultados
        if resultado[0] is not None:
            ultimo_id = resultado[0]
            print(f"O último ID registrado na tabela compras é: {ultimo_id}")

            pgmto = ['cartao', 'boleto', 'pix', 'berries']
                          
            while True:
                ask = int(input("Qual a forma de pagamento?\n"
                                "1 - cartao\n"
                                "2 - boleto\n"
                                "3 - pix\n"
                                "4 - berries\n"))

                if ask in [1, 2, 3, 4]:
                    pgmto_tipo = pgmto[ask - 1]
                    
                    # Verifica se pgmto_tipo está entre os valores válidos
                    if pgmto_tipo not in pgmto:
                        print("Opção de pagamento inválida.")
                        continue

                    sql_update = f"UPDATE compras SET forma_pagamento = '{pgmto_tipo}' WHERE idcompra = {ultimo_id};"
                    cursor.execute(sql_update)
                    conn.commit()
                    break
        else:
            print("Nenhum registro encontrado na tabela compras.")


        
    else:
            print('Usuário ou senha incorretos.')
        

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
    print('9 - Comprar produtos.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
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
        elif opcao == 9:
            comprar_produtos()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
