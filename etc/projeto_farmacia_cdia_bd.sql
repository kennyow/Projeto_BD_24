-- PROJETO FARMACIA -  CDIA - UFPB - 2024
CREATE DATABASE farmacia;
USE farmacia;

CREATE TABLE IF NOT EXISTS medicamentos(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria_regulatoria VARCHAR(40) NOT NULL,
    data_vencimento_registro DATE,
    classe_terapeutica VARCHAR(100) NOT NULL,
    situacao_registro VARCHAR(15) NOT NULL,
    principio_ativo VARCHAR(400) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS clientes(
    idcliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(10) NOT NULL,
    endereco VARCHAR(70) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    isflamengo CHAR(1) NOT NULL,
    isonepiece CHAR(1) NOT NULL,
    issousa CHAR(1) NOT NULL
);

INSERT INTO clientes (nome, telefone, endereco, cidade, isflamengo, isonepiece, issousa) VALUES
('Luke Skywalker', '1234567890', 'Tatooine', 'Mos Eisley', 'N', 'Y', 'N'),
('Leia Organa', '9876543210', 'Alderaan', 'Rebel Base', 'N', 'N', 'N'),
('Han Solo', '5551234567', 'Millennium Falcon', 'Corellia', 'Y', 'N', 'N'),
('Darth Vader', '9998887776', 'Death Star', 'Unknown', 'N', 'N', 'N'),
('Obi-Wan Kenobi', '1112223334', 'Jedi Temple', 'Coruscant', 'N', 'Y', 'N'),
('Yoda', '7778889990', 'Dagobah', 'Swampy Planet', 'N', 'N', 'N'),
('Padmé Amidala', '3334445556', 'Naboo', 'Theed', 'N', 'N', 'N'),
('Chewbacca', '8887776665', 'Kashyyyk', 'Wookiee Planet', 'N', 'N', 'N'),
('R2-D2', '2223334447', 'N/A', 'Outer Space', 'N', 'N', 'N'),
('C-3PO', '4445556663', 'N/A', 'Outer Space', 'N', 'N', 'N'),
('Mace Windu', '6667778889', 'Jedi Temple', 'Coruscant', 'N', 'N', 'Y');
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


