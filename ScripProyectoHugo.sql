CREATE SCHEMA bd_proyectohugo;
use bd_proyectohugo;

CREATE TABLE clientes
( 	documento bigint Primary Key not null,
	nombre char(70),
    movil char(20),
    direccion char(50),
    deuda int,
    a_favor int
);

    

    