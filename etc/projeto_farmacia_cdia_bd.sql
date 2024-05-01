-- PROJETO FARMACIA -  CDIA - UFPB - 2024
CREATE DATABASE farmacia;
USE farmacia;


-- ----------------------------------------------------------------COMANDOS UTILIZADOS NO RELATÓRIO --------------------------------
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


-- ---------------------------------------------------------------- MEDICAMETOS--------------------------------
CREATE TABLE IF NOT EXISTS medicamentos(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria_regulatoria VARCHAR(40) NOT NULL,
    data_vencimento_registro DATE,
    classe_terapeutica VARCHAR(100) NOT NULL,
    mari CHAR(1) NOT NULL,
    situacao_registro VARCHAR(15) NOT NULL,
    principio_ativo VARCHAR(400) NOT NULL,
    estoque INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);

-- ---------------------------------------------------------------- CLIENTES --------------------------------
CREATE TABLE IF NOT EXISTS clientes(
    idcliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(10) NOT NULL,
    email VARCHAR(40),
    isflamengo CHAR(1) NOT NULL,
    isonepiece CHAR(1) NOT NULL,
    issousa CHAR(1) NOT NULL,
    usuario VARCHAR(20) NOT NULL,
    senha VARCHAR(6) NOT NULL
);

INSERT INTO clientes (nome, telefone, email, isflamengo, isonepiece, issousa, usuario, senha) VALUES
('Luke Skywalker', '1234567890', 'luke@rebels.com', 'N', 'Y', 'N', 'skywalker', '123abc'),
('Leia Organa', '9876543210', 'leia@rebels.com', 'N', 'N', 'N', 'organa', '456def'),
('Han Solo', '5551234567', 'han@solo.com', 'Y', 'N', 'N', 'solo', '789ghi'),
('Darth Vader', '9998887776', 'vader@empire.com', 'N', 'N', 'N', 'vader', 'abc123'),
('Obi-Wan Kenobi', '1112223334', 'obiwan@jedi.com', 'N', 'Y', 'N', 'obiwan', 'def456'),
('Yoda', '7778889990', 'yoda@jedi.com', 'N', 'N', 'N', 'yoda', 'ghi789'),
('Padmé Amidala', '3334445556', 'padme@naboo.com', 'N', 'N', 'N', 'padme', '123456'),
('Chewbacca', '8887776665', 'chewie@wookiee.com', 'N', 'N', 'N', 'chewbacca', '456abc'),
('R2-D2', '2223334447', 'r2d2@droids.com', 'N', 'N', 'N', 'r2d2', '789def'),
('C-3PO', '4445556663', 'c3po@droids.com', 'N', 'N', 'N', 'c3po', 'abc456'),
('Mace Windu', '6667778889', 'mace@jedi.com', 'N', 'N', 'Y', 'macewindu', 'def789');


-- ---------------------------------------------------------------- VENDEDORES--------------------------------
CREATE TABLE vendedores(
	idvendedor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
	senha VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO vendedores (nome, usuario, senha)
VALUES
('Monkey D. Luffy', 'luffy', 'strawhat'),
('Roronoa Zoro', 'zoro', 'swordsman'),
('Nami', 'nami', 'navigator'),
('Vinsmoke Sanji', 'sanji', 'cook'),
('Nico Robin', 'robin', 'archaeologist');

CREATE VIEW vendedores_nomes AS
	SELECT idvendedor, nome
    FROM vendedores;

-- ---------------------------------------------------------------- COMPRAS --------------------------------
CREATE TABLE compras (
    idcompra INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    idcliente INT NOT NULL,
    idvendedor INT NOT NULL,
    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10, 2) NOT NULL,
    forma_pagamento varchar(20)  NOT NULL,
    status_pagamento varchar(20)  DEFAULT 'pendente',
    FOREIGN KEY (idcliente) REFERENCES clientes(idcliente),
    FOREIGN KEY (idvendedor) REFERENCES vendedores(idvendedor)
);

-- ---------------------------------------------------------------- ITENS COMPRA --------------------------------
CREATE TABLE itens_compra (
    iditem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    idcompra INT NOT NULL,
    nome_item VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (idcompra) REFERENCES compras(idcompra)
);


    
 -- ---------------------------------------------------------------- ETC --------------------------------   
DROP TABLE compras;
SELECT * FROM compras;
SELECT * FROM vendedores;
SELECT * FROM clientes;
DESC clientes;
DROP TABLE clientes;
DROP TABLE medicamentos;
SELECT * FROM medicamentos;
DROP TABLE vendedores;
SELECT * FROM vendedores_nomes;
