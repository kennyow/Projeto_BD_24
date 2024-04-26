-- PROJETO FARMACIA -  CDIA - UFPB - 2024
CREATE DATABASE farmacia;
USE farmacia;

CREATE TABLE IF NOT EXISTS medicamentos(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria_regulatoria VARCHAR(40) NOT NULL,
    data_vencimento_registro DATE,
    classe_terapeutica VARCHAR(100) NOT NULL,
    mari CHAR(1) NOT NULL,
    situacao_registro VARCHAR(15) NOT NULL,
    principio_ativo VARCHAR(400) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);


-- COMANDOS UTILIZADOS NO RELATÓRIO 

-- Quantidade de Medicamentos
SELECT COUNT(nome) AS QtdeMed
FROM medicamentos;

-- Quantidade de Categoria Regulatória
SELECT DISTINCT(categoria_regulatoria) AS Categoria, COUNT(categoria_regulatoria) AS Quantidade
FROM medicamentos
GROUP BY Categoria
ORDER BY Quantidade DESC;

-- Data do Vencimento perto do dia atual (10 mais próximos)
SELECT nome as MEDICAMENTO, data_vencimento_registro AS Data_vencimento, DATEDIFF(curdate(), data_vencimento_registro) AS PRAZO, situacao_registro AS Situação
FROM medicamentos
WHERE DATEDIFF(curdate(), data_vencimento_registro) < 0
ORDER BY data_vencimento_registro ASC
LIMIT 10; 

-- Quantidade de Situação de Registro
SELECT DISTINCT(situacao_registro) AS Situação, COUNT(situacao_registro) AS Quantidade
FROM medicamentos
GROUP BY Situação
ORDER BY Quantidade DESC;

-- Menor E Maior valor de rempedio com categoria e classe terapeutica
SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, classe_terapeutica AS CLASSE, preco as PREÇO
FROM medicamentos
WHERE preco = (SELECT MIN(preco) FROM medicamentos)
ORDER BY nome;

SELECT nome as NOME, categoria_regulatoria AS CATEGORIA, classe_terapeutica AS CLASSE, preco as PREÇO
FROM medicamentos
WHERE preco = (SELECT MAX(preco) FROM medicamentos)
ORDER BY nome;


