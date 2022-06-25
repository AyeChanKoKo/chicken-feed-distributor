SET SESSION FOREIGN_KEY_CHECKS=0;

/* Drop Tables */

DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS batch;
DROP TABLE IF EXISTS chick;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS feed;
DROP TABLE IF EXISTS Imports;
DROP TABLE IF EXISTS imp_voucher;
DROP TABLE IF EXISTS iventory;
DROP TABLE IF EXISTS med;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS sale_voucher;




/* Create Tables */

CREATE TABLE admin
(
	admin_id int NOT NULL AUTO_INCREMENT,
	username varchar(150) NOT NULL,
	password varchar(150) NOT NULL,
	PRIMARY KEY (admin_id),
	UNIQUE (admin_id),
	UNIQUE (username)
);


CREATE TABLE batch
(
	b_id int NOT NULL AUTO_INCREMENT,
	customer_id int NOT NULL,
	Deposit int,
	status boolean NOT NULL,
	PRIMARY KEY (b_id),
	UNIQUE (b_id),
	UNIQUE (customer_id)
);


CREATE TABLE chick
(
	item_id int NOT NULL,
	price int NOT NULL,
	UNIQUE (item_id)
);


CREATE TABLE customer
(
	customer_id int NOT NULL AUTO_INCREMENT,
	name varchar(150) NOT NULL,
	address varchar(200) NOT NULL,
	phone int NOT NULL,
	PRIMARY KEY (customer_id),
	UNIQUE (customer_id),
	UNIQUE (phone)
);


CREATE TABLE feed
(
	item_id int NOT NULL,
	code varchar(20) NOT NULL,
	price int NOT NULL,
	package varchar(20) NOT NULL,
	UNIQUE (item_id)
);


CREATE TABLE Imports
(
	imp_id int NOT NULL AUTO_INCREMENT,
	item_id int NOT NULL,
	quantity int NOT NULL,
	rate int NOT NULL,
	cost int NOT NULL,
	imp_v_id int NOT NULL,
	t_charge int NOT NULL,
	PRIMARY KEY (imp_id),
	UNIQUE (imp_id)
);


CREATE TABLE imp_voucher
(
	imp_v_id int NOT NULL AUTO_INCREMENT,
	date time NOT NULL,
	PRIMARY KEY (imp_v_id),
	UNIQUE (imp_v_id)
);


CREATE TABLE items
(
	item_id int NOT NULL AUTO_INCREMENT,
	item_name varchar(150) NOT NULL,
	item_type int NOT NULL,
	PRIMARY KEY (item_id),
	UNIQUE (item_id)
);


CREATE TABLE iventory
(
	item_id int NOT NULL,
	quantity int NOT NULL,
	UNIQUE (item_id)
);


CREATE TABLE med
(
	item_id int NOT NULL,
	package varchar(20) NOT NULL,
	price int NOT NULL,
	UNIQUE (item_id)
);


CREATE TABLE sales
(
	sale_id int NOT NULL AUTO_INCREMENT,
	b_id int NOT NULL,
	item_id int NOT NULL,
	quantity int NOT NULL,
	rate int NOT NULL,
	sv_id int NOT NULL,
	PRIMARY KEY (sale_id),
	UNIQUE (sale_id),
	UNIQUE (b_id),
	UNIQUE (item_id),
	UNIQUE (sv_id)
);


CREATE TABLE sale_voucher
(
	sv_id int NOT NULL AUTO_INCREMENT,
	date datetime,
	t_charge int NOT NULL,
	PRIMARY KEY (sv_id),
	UNIQUE (sv_id)
);



/* Create Foreign Keys */

ALTER TABLE sales
	ADD FOREIGN KEY (b_id)
	REFERENCES batch (b_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE batch
	ADD FOREIGN KEY (customer_id)
	REFERENCES customer (customer_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE Imports
	ADD FOREIGN KEY (imp_v_id)
	REFERENCES imp_voucher (imp_v_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE chick
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE feed
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE Imports
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE iventory
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE med
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE sales
	ADD FOREIGN KEY (item_id)
	REFERENCES items (item_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE sales
	ADD FOREIGN KEY (sv_id)
	REFERENCES sale_voucher (sv_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



