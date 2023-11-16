CREATE DATABASE mirvaj;
USE mirvaj;

CREATE TABLE rol(
	idRol INT NOT NULL PRIMARY KEY,
  nameRol VARCHAR(15) NOT NULL
);

INSERT INTO rol VALUES (1, "Administrador");
INSERT INTO rol VALUES (2, "Cliente");

CREATE TABLE EST_ACTIVE(
	idAct INT AUTO_INCREMENT PRIMARY KEY,
    estAct VARCHAR(10) NOT NULL
);

INSERT INTO EST_ACTIVE(estAct) VALUES('INACTIVO'); -- Cambiar entre activo o inactivo

CREATE TABLE userstbl (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `emailUser` varchar(60) NOT NULL,
  `passwordUser` varchar(255) NOT NULL, -- Cambiar tamaño para almacenar contraseñas cifradas
  rol INT,
  `active` boolean not null DEFAULT 1,
  FOREIGN KEY (rol) REFERENCES rol(idRol),
  PRIMARY KEY (`idUser`)
);

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

CREATE TABLE `typeeventstbl` (
  `idTypeEvent` int NOT NULL AUTO_INCREMENT,
  `nameTypeEvent` varchar(30) NOT NULL,
  `descriptionTypeEvent` varchar(60) NOT NULL,
    idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct),
  PRIMARY KEY (`idTypeEvent`)
);

CREATE TABLE amountPeople(
	idAmountPe INT AUTO_INCREMENT PRIMARY KEY,
    AmountPe INT NOT NULL,
    costAmountPe INT NOT NULL,
    idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct)
);
CREATE TABLE additionalMob(
	idAdMob INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nameAdMob VARCHAR(25) NOT NULL,
    costAdMob INT NOT NULL,
    idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct)
);

CREATE TABLE additionalDec(
	idAdDec INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nameAdDec VARCHAR(25) NOT NULL,
    costAdDec INT NOT NULL,
	idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct)
);
CREATE TABLE additionalAli(
	idAdAli INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nameAdAli VARCHAR(25) NOT NULL,
    costAdAli INT NOT NULL,
	idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct)
);
CREATE TABLE othersServ(
	idOtServ INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nameOtServ VARCHAR(25) NOT NULL,
    costOtServ INT NOT NULL,
	idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct)
);
CREATE TABLE eventsTbl(
	idEvent INT AUTO_INCREMENT PRIMARY KEY,
    idClient INT NOT NULL,
    idTypeEvent INT NOT NULL,
    idAmountPe INT NOT NULL,
    idAdMob INT NOT NULL,
    idAdDec INT NOT NULL,
    idAdAli INT NOT NULL,
    idOtServ INT NOT NULL,
	idAct INT NOT NULL,
    FOREIGN KEY (idAct) REFERENCES EST_ACTIVE(idAct),
    FOREIGN KEY (idClient) REFERENCES clientsTbl(idCliente),
    FOREIGN KEY (idTypeEvent) REFERENCES typeeventstbl(idTypeEvent),
    FOREIGN KEY (idAmountPe) REFERENCES amountPeople(idAmountPe),
    FOREIGN KEY (idAdMob) REFERENCES additionalMob(idAdMob),
    FOREIGN KEY (idAdDec) REFERENCES additionalDec(idAdDec),
    FOREIGN KEY (idAdAli) REFERENCES additionalAli(idAdAli),
    FOREIGN KEY (idOtServ) REFERENCES othersServ(idOtServ)
);

SELECT * FROM userstbl;
