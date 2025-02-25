create database db_feedback;
use db_feedback;
create table tb_comentarios(
	nome varchar(100) not null,
    comentario text not null,
    cod_comentario int auto_increment primary key,
    data_hora datetime not null
    
);