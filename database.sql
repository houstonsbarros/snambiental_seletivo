create database biblioteca;

use biblioteca;

create table livros_livro (
    id int not null auto_increment,
    vTitulo varchar(35) not null,
    vAutor varchar(20) not null,
    iAno_publicacao int not null,
    vEditora varchar(15) not null,
    primary key (id)
);

create table usuarios_usuario (
    id int not null auto_increment,
    vNome varchar(80) not null,
    dNascimento date not null,
    vCpf varchar(11) not null,
    vEmail varchar(50) not null,
    primary key (id)
);

create table emprestimos_emprestimo (
    id int not null auto_increment,
    livro_id int not null,
    usuario_id int not null,
    dData_emprestimo date not null,
    dData_devolucao date not null,
    primary key (id),
    foreign key (livro_id) references livros_livro(id),
    foreign key (usuario_id) references usuarios_usuario(id)
);
insert into livros_livro(vTitulo, vAutor, iAno_publicacao, vEditora) values
('Dom Quixote', 'Miguel de Cervantes', 1605, 'Editora'),
('1984', 'George Orwell', 1949, 'Editora'),
('O Grande Gatsby', 'F. Scott Fitzgerald', 1925, 'Editora'),
('Orgulho e Preconceito', 'Jane Austen', 1813, 'Editora'),
('Cem Anos de Solidão', 'Gabriel García Márquez', 1967, 'Editora'),
('O Apanhador no Campo de Centeio', 'J.D. Salinger', 1951, 'Editora'),
('Crime e Castigo', 'Fiódor Dostoiévski', 1866, 'Editora'),
('Ulisses', 'James Joyce', 1922, 'Editora'),
('Em Busca do Tempo Perdido', 'Marcel Proust', 1913, 'Editora'),
('Moby Dick', 'Herman Melville', 1851, 'Editora');

insert into usuarios_usuario(vNome, dNascimento, vCpf, vEmail) values
('Elias Pietro Davi Almada', '2003-05-01', '99854163334', 'elias_almada@gmail.com'),
('Emilly Marlene Vanessa Fernandes', '1995-03-15', '95894876370', 'emilly_marlene_fernandes@gmail.com'),
('Débora Beatriz da Conceição', '1963-03-20', '14609619350', 'debora.beatriz.daconceicao@gmail.com'),
('Geraldo Carlos Eduardo André Aragão', '1944-04-20', '90292267304', 'geraldo-aragao73@gmail.com'),
('Danilo Lucas Carlos Almeida', '1978-04-22', '72426968362', 'danilo-almeida94@gmail.com');

insert into emprestimos_emprestimo(livro_id, usuario_id, dData_emprestimo, dData_devolucao) values
(1, 1, '2023-05-09', '2023-05-15'),
(2, 2, '2023-05-13', '2023-05-20');