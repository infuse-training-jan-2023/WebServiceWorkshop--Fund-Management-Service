import sqlite3

connection = sqlite3.connect('todo.db')

with open('DB/schema.sql') as f:
	connection.executescript(f.read())

cursor = connection.cursor()
cursor.execute("INSERT INTO Accounts (userName, emailID, mobileNum, city, balance) VALUES (?, ?, ?, ?, ?)", ('Omkar', 'omkar.savoikar@infuse.it', '1234567890', 'Ponda', '1000'))
cursor.execute("INSERT INTO Deposits (accountNum, depositAmount) VALUES(?, ?)", ('1', '1000'))
cursor.execute("INSERT INTO Loans (loanAmt, timePeriod, interestRate, payBackAmt, amtPaid, amtRemaining, accountNum) VALUES (?, ?, ?, ?, ?, ?, ?)", ('10000', '12', '3.5', '14200', '1000', '13200', '1'))
cursor.execute("INSERT INTO LoanDeposits (depositAmount, loanID) VALUES (?, ?)", ('1000', '1'))
connection.commit()
connection.close()