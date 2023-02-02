import sqlite3
import json

class Repository:
	DBPATH = "./todo.db"
  Balance = 0
  status = False

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

    @staticmethod
    def create_account(name, email, mob, city):
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            insert_cursor = c.execute('INSERT INTO Accounts (userName, emailID, mobileNum, city, balance) VALUES (?, ?, ?, ?, ?)',
            (name, email, mob, city, Repository.Balance))
            conn.commit()
            return{
                'accountNum': insert_cursor.lastrowid,
                'userName': name,
                'emailID': email,
                'mobileNum': mob,
                'city': city,
                'balance': Repository.Balance
            }
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def get_account_details(bank_acc_no):
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from Accounts where status=true AND accountNum=?',(bank_acc_no, ))
            print("Rows Value: " ,rows)
            return rows
        except Exception as e:
            raise Exception('Error: ',e)

    @staticmethod
    def get_all_account_details():
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from Accounts where status=true')
            print("Rows Value: " ,rows)
            return rows
        except Exception as e:
            raise Exception('Error: ',e)

    @staticmethod
    def deposite_amount(bank_acc_no, amount):

        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            fetch_cursor = c.execute('select balance from Accounts where accountNum=?', (bank_acc_no, ))
            balance = fetch_cursor.fetchone()[0]
            update_balance =  balance + amount
            insert_cursor = c.execute('INSERT INTO Deposits (accountNum, depositAmount) VALUES(?, ?)',
            (bank_acc_no, amount))
            update_cursor = c.execute('UPDATE Accounts SET balance=? WHERE accountNum=?', (update_balance, bank_acc_no, ))
            conn.commit()
            return{
                'id': insert_cursor.lastrowid,
                'Bank_Account_Number': bank_acc_no,
                'Amount': amount
            }
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def get_deposite_amount(bank_acc_no):
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from Deposits where accountNum=?', (bank_acc_no, ))
            # print("Row Values:",rows)
            return rows
        except Exception as e:
            raise Exception('Error: ', e)


    @staticmethod
    def delete_user(bank_acc_no):
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            fetch_status = c.execute('select status from Accounts where accountNum=?', (bank_acc_no, ))
            if fetch_status == 0:
                raise TypeError("Account Dosen't Exist")
            rows = c.execute('UPDATE Accounts SET status=? WHERE accountNum=?', (0, bank_acc_no, ))
            conn.commit()
            return{
                'Bank_Account_Number': bank_acc_no,
                'status': False
            }
        except Exception as e:
            raise Exception('Error: ', e)