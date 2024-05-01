import MySQLdb

class DataProvider:
    def __init__(self, name, host, user, pwd):
        self.conn = None
        self.name = name
        self.host = host
        self.user = user
        self.pwd = pwd

    def open(self):
        try:
            self.conn = MySQLdb.connect(
                db=self.name,
                host=self.host,
                user=self.user,
                passwd=self.pwd
            )

            return True

        except MySQLdb.Error as e:
            print(f"Connection error on MySQL Server: {e}")
            return False


    def close(self):
        if self.conn:
            self.conn.close()

    def list(self):
        conn =  self.open()
        cursor = self.conn.cursor()

        cursor.execute(f"SELECT * FROM medicamentos")
        produtos = cursor.fetchall()

        medicine_list = []
        for produto in produtos:
            medicine_list.append({})
            medicine_list[-1]['id'] = produto[0]
            medicine_list[-1]['product'] = produto[1]
            medicine_list[-1]['category'] = produto[2]
            medicine_list[-1]['limit_date'] = produto[3]
            medicine_list[-1]['therapeutic_class'] = produto[4]
            medicine_list[-1]['status'] = produto[5]
            medicine_list[-1]['active'] = produto[6]
            medicine_list[-1]['price'] = produto[7]

        self.close()

        return medicine_list

    def create(self, nome, categoria, vencimento, classe, situacao, principio, preco):
        self.open()
        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO medicamentos (id, nome, categoria_regulatoria, data_vencimento_registro, classe_terapeutica, situacao_registro, principio_ativo, preco) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)",
                       (nome, categoria, vencimento, classe, situacao, principio, float(preco)))
        self.conn.commit()

        self.close()

    def update(self, id, nome, categoria, vencimento, classe, situacao, principio, preco):
        self.open()
        cursor = self.conn.cursor()

        cursor.execute("UPDATE medicamentos SET nome=%s, categoria_regulatoria=%s, data_vencimento_registro=%s, classe_terapeutica=%s, situacao_registro=%s, principio_ativo=%s, preco=%s WHERE id=%s",
                       (nome, categoria, vencimento, classe, situacao, principio, float(preco), id))
        self.conn.commit()

        self.close()

    def delete(self, id):
        self.open()
        cursor  = self.conn.cursor()

        cursor.execute("DELETE FROM medicamentos WHERE id=%s", (id,))

        self.conn.commit()

        self.close()

        if cursor.rowcount == 1:
            return True

        return False
    
    def log(self):
        self.open()
        cursor = self.conn.cursor()

        log = ""

        log += 'RELATÓRIO MEDICAMENTOS\n'
        log += '------------------------------------------\n'


        cursor.execute("SELECT COUNT(nome) AS QtdeMed FROM medicamentos;")
        result = cursor.fetchone()
        log += f"Quantidade de Medicamentos: {result[0]}\n"
        log += '------------------------------------------\n'

        log += 'Quantidade por Categoria Regulatória\n'
        log += '------------------------------------------\n'
        cursor.execute("SELECT DISTINCT(categoria_regulatoria) AS Categoria, COUNT(categoria_regulatoria) AS Quantidade FROM medicamentos GROUP BY Categoria ORDER BY Quantidade DESC;")
        results = cursor.fetchall()
        for row in results:
            log += str(row) + "\n"
        log += '------------------------------------------\n'
        log += 'Data do Vencimento perto do dia de hoje (10 mais próximos)\n'
        log += '------------------------------------------\n'
        cursor.execute("SELECT nome as MEDICAMENTO, data_vencimento_registro AS Data_vencimento, DATEDIFF(curdate(), data_vencimento_registro) AS PRAZO, situacao_registro AS Situação FROM medicamentos WHERE DATEDIFF(curdate(), data_vencimento_registro) < 0 ORDER BY data_vencimento_registro ASC LIMIT 10;")
        results = cursor.fetchall()
        for row in results:
            log += str(row) + "\n"
        log += '------------------------------------------\n'
        log += 'Quantitativo de Situação de Registro\n'
        log += '------------------------------------------\n'
        cursor.execute("SELECT DISTINCT(situacao_registro) AS Situação, COUNT(situacao_registro) AS Quantidade FROM medicamentos GROUP BY Situação ORDER BY Quantidade DESC;")
        results = cursor.fetchall()
        for row in results:
            log += str(row) + "\n"
        log += '------------------------------------------\n'
        log += 'Remédios de menor valor e sua categoria\n'
        log += '------------------------------------------\n'
        cursor.execute("SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, preco as PREÇO FROM medicamentos WHERE preco = (SELECT MIN(preco) FROM medicamentos) ORDER BY nome;")
        results = cursor.fetchall()
        for row in results:
            log += str(row) + "\n"
        log += '------------------------------------------\n'
        log += 'Remédios de maior valor e sua categoria\n'
        log += '------------------------------------------\n'
        cursor.execute("SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, preco as PREÇO FROM medicamentos WHERE preco = (SELECT MAX(preco) FROM medicamentos) ORDER BY nome;")
        results = cursor.fetchall()
        for row in results:
            log += str(row) + "\n"

        self.conn.commit()

        self.close()

        return log

