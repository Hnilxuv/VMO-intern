create database Bank;

use Bank

CREATE TABLE account_bank(
	id int PRIMARY KEY NOT NULL IDENTITY(1,1),
	name nvarchar(50) NOT NULL,
	acc_no nvarchar(50) NOT NULL,
	balance int NOT NULL
);

INSERT account_bank(name, acc_no, balance) VALUES ( N'Linh', N'33333', 1000000),( N'Vũ', N'44444', 1000000);