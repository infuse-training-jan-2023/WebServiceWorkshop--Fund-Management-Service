PRAGMA foreign_keys = ON;
CREATE TABLE "Accounts"(
	"accountNum" INTEGER PRIMARY KEY AUTOINCREMENT,
	"userName" VARCHAR [50] NOT NULL,
	"emailID" VARCHAR [20] NOT NULL,
	"mobileNum" VARCHAR [30] NOT NULL,
	"city" VARCHAR [20] NOT NULL,
	"balance" INTEGER NOT NULL,
	"status" INTEGER DEFAULT 1
);
CREATE TABLE "Deposits"(
	"depositID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"depositAmount" INTEGER NOT NULL,
	"accountNum" INTEGER NOT NULL,
	FOREIGN KEY ("accountNum") REFERENCES Accounts("accountNum")
);
CREATE TABLE "Loans"(
	"loanID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"loanAmt" INTEGER NOT NULL,
	"timePeriod" INTEGER NOT NULL,
	"interestRate" DECIMAL (3, 2) NOT NULL,
	"payBackAmt" INTEGER NOT NULL,
	"amtPaid" INTEGER NOT NULL,
	"amtRemaining" INTEGER NOT NULL,
	"status" INTEGER DEFAULT 1,
	"accountNum" INTEGER NOT NULL,
	FOREIGN KEY ("accountNum") REFERENCES Accounts("accountNum")
);
CREATE TABLE "LoanDeposits"(
	"loanDepositID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"depositAmount" INTEGER NOT NULL,
	"loanID" INTEGER NOT NULL,
	FOREIGN KEY ("loanID") REFERENCES Loans("loanID")
);