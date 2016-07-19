/*
 * Doors database 
 *
 */

DROP TABLE IF EXISTS doortrackerDatabase.doors;
DROP TABLE IF EXISTS doortrackerDatabase.events;

USE doortrackerDatabase;
CREATE TABLE doors( 
	doorID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	doorName varchar(255) NULL);

CREATE TABLE events(
	eventID int NOT NULL AUTO_INCREMENT,
	doorID int NOT NULL,
	PRIMARY KEY(eventID),
	FOREIGN KEY (doorID) REFERENCES doors(doorID));

INSERT INTO doors VALUES (	"Chambre à Coucher", 
							"Porte Patio", 
							"Porte Avant",
							"Shed",
							"Bureau");