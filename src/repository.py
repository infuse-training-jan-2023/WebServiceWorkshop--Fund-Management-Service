import sqlite3
import json

class Repository:
	NOT_STARTED = "Not Started"
	DBPATH = "./todo.db"

	@staticmethod
	def connect_db():
		return sqlite3.connect(Repository.DBPATH)
	
	@staticmethod
	def add_loan_account(loan_amt, time_period, interest_rate, account_num):
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			SI = (loan_amt * time_period * interest_rate) / 100
			payback_amount = loan_amt + SI
			insert_cursor = c.execute("INSERT INTO Loans (loanAmt, timePeriod, interestRate, payBackAmt, amtPaid, amtRemaining, status, accountNum) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (loan_amt, time_period, interest_rate, payback_amount, 0, payback_amount, True, account_num))
			conn.commit()
			return{
				'loanID': insert_cursor.lastrowid,
				'loanAmt': loan_amt,
				'timePeriod': time_period,
				'interestRate': interest_rate,
				'payBackAmt': payback_amount,
				'amtPaid': 0,
				'amtRemaining': payback_amount,
				'status': 1,
				'accountNum': account_num
			}
		except Exception as e:
			raise Exception("Error: ", e)
			
	@staticmethod
	def get_loan_account(id):
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			row = c.execute("SELECT * FROM Loans WHERE loanID = " + str(id))
			return row
		except Exception as e:
			raise Exception("Error: ", e)
	
	@staticmethod
	def get_all_loan_accounts():
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			rows = c.execute("SELECT * FROM Loans")
			return rows
		except Exception as e:
			raise Exception("Error: ", e)
	
	@staticmethod
	def get_all_loan_ammount_sum():
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			row = c.execute("SELECT SUM(loanAmt) FROM Loans")
			return row
		except Exception as e:
			raise Exception("Error: ", e)
	
	@staticmethod
	def add_loan_deposit(deposit_amt, loan_id):
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			# row = c.execute("SELECT status, payBackAmt, amtPaid, amtRemaining FROM Loans WHERE loanID = " + str(loan_id))
			row = Repository.get_loan_account(loan_id)
			for x in row:
				status = x[7]
				amtPaid = x[5]
				amtRemaining = x[6]
			if status != 1:
				raise TypeError("Loan amount paid fully or Account doesn't exist")
			insert_cursor = c.execute("INSERT INTO LoanDeposits (depositAmount, loanID) VALUES (?, ?)", (deposit_amt, loan_id))
			conn.commit()

			amtPaid += deposit_amt
			amtRemaining -= deposit_amt
			if (amtRemaining <= 0):
				insert_cursor = c.execute("UPDATE Loans SET amtPaid = ?, amtRemaining = ?, status = ? WHERE loanID = ?", (amtPaid, 0, 0, loan_id, ))
			else:
				insert_cursor = c.execute("UPDATE Loans SET amtPaid = ?, amtRemaining = ? WHERE loanID = ?", (amtPaid, amtRemaining, loan_id, ))
			conn.commit()
			return{
				'loanDepositID': insert_cursor.lastrowid,
				'depositAmount': deposit_amt,
				'loanID': loan_id
			}
		except Exception as e:
			raise Exception("Error: ", e)

	@staticmethod
	def get_all_loan_deposit_sum():
		try:
			conn = Repository.connect_db()
			c = conn.cursor()
			row = c.execute("SELECT SUM(depositAmount) FROM LoanDeposits")
			return row
		except Exception as e:
			raise Exception("Error: ", e)