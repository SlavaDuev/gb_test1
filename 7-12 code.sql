CREATE DATABASE Друзья_человека;
USE Друзья_человека;

-- Таблица для всех животных
CREATE TABLE Животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(100),
    вид VARCHAR(100),
    команда VARCHAR(255),
    дата_рождения DATE
);

-- Таблица для домашних животных
CREATE TABLE Домашние_животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(100),
    команда VARCHAR(255),
    дата_рождения DATE
);

-- Таблица для вьючных животных
CREATE TABLE Вьючные_животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(100),
    команда VARCHAR(255),
    дата_рождения DATE
);

-- Заполнение таблицы домашних животных
INSERT INTO Домашние_животные (имя, команда, дата_рождения)
VALUES 
('Барсик', 'сидеть', '2021-03-10'),
('Рекс', 'апорт', '2020-06-21'),
('Пушок', 'бежать', '2022-11-05');

-- Заполнение таблицы вьючных животных
INSERT INTO Вьючные_животные (имя, команда, дата_рождения)
VALUES 
('Буцефал', 'идти', '2018-04-10'),
('Ганнибал', 'стоять', '2017-08-14'),
('Тяжеловоз', 'нести', '2019-02-23');
