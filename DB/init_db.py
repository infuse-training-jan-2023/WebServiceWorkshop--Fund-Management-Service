import sqlite3

connection = sqlite3.connect('todo.db')

with open('DB/schema.sql') as f:
	connection.executescript(f.read())

cursor = connection.cursor()
cursor.execute("INSERT INTO Accounts (username, emailID, mobile_number, city, balance) VALUES (?, ?, ?, ?, ?)", ('Omkar', 'omkar.savoikar@infuse.it', '1234567890', 'Ponda', '1000'))
cursor.execute("INSERT INTO Deposits (account_number, deposit_amount) VALUES(?, ?)", ('1', '1000'))
cursor.execute("INSERT INTO Loans (loan_amount, time_period, interest_rate, payback_amount, amt_paid, amt_remaining, account_number) VALUES (?, ?, ?, ?, ?, ?, ?)", ('10000', '12', '3.5', '14200', '1000', '13200', '1'))
cursor.execute("INSERT INTO LoanDeposits (deposit_amount, loan_ID) VALUES (?, ?)", ('1000', '1'))
connection.commit()
connection.close()