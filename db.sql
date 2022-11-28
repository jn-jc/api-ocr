CREATE DATABASE ocr_db;

CREATE TABLE tienda(
  `id_tienda` int NOT NULL AUTO_INCREMENT,
  `sucursal` varchar(30) NOT NULL,
  PRIMARY KEY(`id_tienda`)
);

CREATE TABLE plan(
  `id_plan` int NOT NULL AUTO_INCREMENT,
  `sucursal` varchar(50) NOT NULL,
  PRIMARY KEY(`id_plan`)
);

CREATE TABLE usuarios(
  id_usuario int NOT NULL AUTO_INCREMENT,
  id_tienda int NOT NULL,
  nombre_usuario varchar(50) NOT NULL,
  apellido_usuario varchar(50) NOT NULL,
  email_usuario varchar(60) NOT NULL,
  PRIMARY KEY(id_usuario),
  FOREIGN KEY(id_tienda) REFERENCES tienda(id_tienda)
);

CREATE TABLE clientes(
  id_cliente int NOT NULL AUTO_INCREMENT,
  tipo_documento varchar(15) NOT NULL,
  no_documento int NOT NULL,
  nombre_cliente varchar(50) NOT NULL,
  apellido_cliente varchar(50) NOT NULL,
  email_cliente varchar(60) NOT NULL,
  fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(id_cliente)
);

CREATE TABLE plan_clientes(
  id_plan_cliente int NOT NULL AUTO_INCREMENT,
  id_cliente int NOT NULL,
  id_plan int NOT NULL,
  PRIMARY KEY(id_plan_cliente),
  FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE imagen(
  id_imagen int NOT NULL AUTO_INCREMENT,
  id_cliente int NOT NULL,
  id_plan_cliente int NOT NULL,
  nombre_archivo varchar(50) NOT NULL,
  PRIMARY KEY(id_imagen),
  FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
);