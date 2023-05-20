--DDL (DATA DEFINOCION LENGUAJE)
--CREATE CREA DB,COLUMNAS O INDICES
--ALTER MODIFICA LA 
--DROP BORRA LA TABLA



CREATE DATABASE prueba;
--creando mi primera tabla en postgres
CREATE TABLE alumnos (
id SERIAL NOT NULL PRIMARY KEY,
nombre TEXT NOT NULL,
apellido_materno TEXT NOT NULL,
apellido_paterno TEXT NULL,
correo TEXT NOT NULL UNIQUE,
fecha_nacimiento DATE ,
activo BOOLEAN DEFAULT true
);


-- DML (DATA MANIPULATION LANGUAGE)
-- INSERT > Insertar data a las tablas
-- SELECT > Seleccionar la data de las tablas
-- UPDATE > Actualizar la informacion contenida en las tablas
-- DELETE > Eliminar la informacion de las tablas




INSERT INTO alumnos (id,nombre,apellido_paterno,apellido_materno,correo,fecha_nacimiento,activo)VALUES
(DEFAULT,'RITJOE','MUJICA','MONTERO','eojtir@gmail.com','1984-07-29',DEFAULT);
INSERT INTO alumnos (id,nombre,apellido_paterno,apellido_materno,correo,fecha_nacimiento,activo)VALUES
(DEFAULT, 'Juana', 'Martinez', 'Manrique', 'jmartinez@gmail.com', '1992-11-01', DEFAULT),
(DEFAULT, 'Pedro', 'Choquehuanca', 'Gil', 'pchoquehuanca@gmail.com', '2000-05-15', false),
(DEFAULT, 'Martin', 'Ancco', 'Perez', 'mancco@gmail.com', '1998-09-25', DEFAULT),
(DEFAULT, 'Roxana', 'Juarez', 'Rodriguez', 'rjuarez@gmail.com', '2005-02-09', false);

SELECT * FROM alumnos--todos los registros
