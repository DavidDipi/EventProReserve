CREATE DATABASE mirvaj;
USE mirvaj;

CREATE TABLE clientsTbl(
	idCliente INT AUTO_INCREMENT PRIMARY KEY,
  `fullnameClient` varchar(60) NOT NULL,
  `phoneClient` varchar(11) NOT NULL,
  idUser INT,
  FOREIGN KEY (idUser) REFERENCES userstbl(idUser)
);

CREATE TABLE adminTbl(
	idAdmin INT AUTO_INCREMENT PRIMARY KEY,
  `fullnameAdmin` varchar(60) NOT NULL,
  `phoneAdmin` varchar(11) NOT NULL,
  idUser INT,
  FOREIGN KEY (idUser) REFERENCES userstbl(idUser)
);

CREATE TABLE userstbl (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `emailUser` varchar(60) NOT NULL,
  `passwordUser` varchar(255) NOT NULL, -- Cambiar tamaño para almacenar contraseñas cifradas
  rol INT,
  FOREIGN KEY (rol) REFERENCES rol(idRol),
  PRIMARY KEY (`idUser`)
);

CREATE TABLE rol(
	idRol INT NOT NULL PRIMARY KEY,
    nameRol VARCHAR(15) NOT NULL
);

CREATE TABLE `typeeventstbl` (
  `idTypeEvent` int NOT NULL AUTO_INCREMENT,
  `nameTypeEvent` varchar(30) NOT NULL,
  `descriptionTypeEvent` varchar(60) NOT NULL,
  PRIMARY KEY (`idTypeEvent`)
);
CREATE TABLE `decorationtbl` (
  `idDecoration` int NOT NULL AUTO_INCREMENT,
  `typeDecoration` varchar(50) DEFAULT NULL,
  `precioDecoration` int DEFAULT NULL,
  PRIMARY KEY (`idDecoration`)
);

SELECT * FROM userstbl;
INSERT INTO rol VALUES (1, "Administrador");
INSERT INTO rol VALUES (2, "Cliente");
