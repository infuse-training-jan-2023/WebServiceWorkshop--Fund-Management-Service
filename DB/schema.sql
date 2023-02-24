PRAGMA foreign_keys = ON;
CREATE TABLE "Accounts"(
	"account_number" INTEGER PRIMARY KEY AUTOINCREMENT,
	"username" VARCHAR [50] NOT NULL,
	"emailID" VARCHAR [20] NOT NULL,
	"mobile_number" VARCHAR [30] NOT NULL,
	"city" VARCHAR [20] NOT NULL,
	"balance" INTEGER NOT NULL,
	"status" INTEGER DEFAULT 1
);
CREATE TABLE "Deposits"(
	"deposit_ID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"deposit_amount" INTEGER NOT NULL,
	"account_number" INTEGER NOT NULL,
	FOREIGN KEY ("account_number") REFERENCES Accounts("account_number")
);
CREATE TABLE "Loans"(
	"loan_ID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"loan_amount" INTEGER NOT NULL,
	"time_period" INTEGER NOT NULL,
	"interest_rate" DECIMAL (3, 2) NOT NULL,
	"payback_amount" INTEGER NOT NULL,
	"amt_paid" INTEGER NOT NULL,
	"amt_remaining" INTEGER NOT NULL,
	"status" INTEGER DEFAULT 1,
	"account_number" INTEGER NOT NULL,
	FOREIGN KEY ("account_number") REFERENCES Accounts("account_number")
);
CREATE TABLE "LoanDeposits"(
	"loanDepositID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"deposit_amount" INTEGER NOT NULL,
	"loan_ID" INTEGER NOT NULL,
	FOREIGN KEY ("loan_ID") REFERENCES Loans("loan_ID")
);