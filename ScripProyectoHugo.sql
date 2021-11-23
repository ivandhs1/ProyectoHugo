CREATE SCHEMA bd_proyectohugo;
use bd_proyectohugo;

CREATE TABLE clientes
( 	documento int Primary Key not null,
	nombre char(70),
    movil char(20),
    saldo int
);
    