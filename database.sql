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