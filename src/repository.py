import sqlite3

class Repository:

    def __init__(self) -> None:
        self.db_path = './todo.db'
        self.connection = None
        self.Balance = 0
        self.status = False

    def connect_db(self):
        if self.connection is None:
            self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)



    def add_loan_account(self, loan_amt, time_period, interest_rate, account_num):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            SI = (loan_amt * time_period * interest_rate) / 100
            payback_amount = loan_amt + SI
            insert_cursor = cursor.execute("INSERT INTO Loans (loanAmt, timePeriod, interestRate, payBackAmt, amtPaid, amtRemaining, status, accountNum) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (loan_amt, time_period, interest_rate, payback_amount, 0, payback_amount, True, account_num))
            self.connection.commit()
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


    def get_loan_account(self, id):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = cursor.execute("SELECT * FROM Loans WHERE loanID = " + str(id))
            return row
        except Exception as e:
            raise Exception("Error: ", e)


    def get_all_loan_accounts(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute("SELECT * FROM Loans")
            return rows
        except Exception as e:
            raise Exception("Error: ", e)


    def get_all_loan_amount_sum(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = cursor.execute("SELECT SUM(loanAmt) FROM Loans")
            return row
        except Exception as e:
            raise Exception("Error: ", e)


    def add_loan_deposit(self,deposit_amt, loan_id):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = Repository.get_loan_account(loan_id)
            for x in row:
                status = x[7]
                amtPaid = x[5]
                amtRemaining = x[6]
            if status != 1:
                raise TypeError("Loan amount paid fully or Account doesn't exist")
            insert_cursor = cursor.execute("INSERT INTO LoanDeposits (depositAmount, loanID) VALUES (?, ?)", (deposit_amt, loan_id))
            self.connection.commit()

            amtPaid += deposit_amt
            amtRemaining -= deposit_amt
            if (amtRemaining <= 0):
                insert_cursor = cursor.execute("UPDATE Loans SET amtPaid = ?, amtRemaining = ?, status = ? WHERE loanID = ?", (amtPaid, 0, 0, loan_id, ))
            else:
                insert_cursor = cursor.execute("UPDATE Loans SET amtPaid = ?, amtRemaining = ? WHERE loanID = ?", (amtPaid, amtRemaining, loan_id, ))
            self.connection.commit()
            return{
                'loanDepositID': insert_cursor.lastrowid,
                'depositAmount': deposit_amt,
                'loanID': loan_id
            }
        except Exception as e:
            raise Exception("Error: ", e)


    def get_all_loan_deposit_sum(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = cursor.execute("SELECT SUM(depositAmount) FROM LoanDeposits")
            return row
        except Exception as e:
            raise Exception("Error: ", e)


    def create_account(self,name, email, mob, city):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            insert_cursor = cursor.execute('INSERT INTO Accounts (userName, emailID, mobileNum, city, balance) VALUES (?, ?, ?, ?, ?)',
            (name, email, mob, city, self.Balance))
            self.connection.commit()
            return{
                'accountNum': insert_cursor.lastrowid,
                'userName': name,
                'emailID': email,
                'mobileNum': mob,
                'city': city,
                'balance': self.Balance
            }
        except Exception as e:
            raise Exception('Error: ', e)


    def get_account_details(self,bank_acc_no):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute('select * from Accounts where status=true AND accountNum=?',(bank_acc_no, ))
            print("Rows Value: " ,rows)
            return rows
        except Exception as e:
            raise Exception('Error: ',e)


    def get_all_account_details(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute('select * from Accounts where status=true')
            print("Rows Value: " ,rows)
            return rows
        except Exception as e:
            raise Exception('Error: ',e)


    def deposit_amount(self, bank_acc_no, amount):

        try:
            self.connect_db()
            cursor = self.connection.cursor()
            fetch_cursor = cursor.execute('select balance from Accounts where accountNum=?', (bank_acc_no, ))
            balance = fetch_cursor.fetchone()[0]
            update_balance =  balance + amount
            insert_cursor = cursor.execute('INSERT INTO Deposits (accountNum, depositAmount) VALUES(?, ?)',
            (bank_acc_no, amount))
            update_cursor = cursor.execute('UPDATE Accounts SET balance=? WHERE accountNum=?', (update_balance, bank_acc_no, ))
            self.connection.commit()
            return{
                'id': insert_cursor.lastrowid,
                'Bank_Account_Number': bank_acc_no,
                'Amount': amount
            }
        except Exception as e:
            raise Exception('Error: ', e)


    def get_deposit_amount(self, bank_acc_no):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute('select * from Deposits where accountNum=?', (bank_acc_no, ))
            return rows
        except Exception as e:
            raise Exception('Error: ', e)



    def delete_user(self, bank_acc_no):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            fetch_status = cursor.execute('select status from Accounts where accountNum=?', (bank_acc_no, ))
            if fetch_status.fetchone()[0] == 0:
                raise TypeError("Account Dosen't Exist")
            rows = cursor.execute('UPDATE Accounts SET status=? WHERE accountNum=?', (0, bank_acc_no, ))
            self.connection.commit()
            return{
                'Bank_Account_Number': bank_acc_no,
                'status': self.status
            }
        except Exception as e:
            raise Exception('Error: ', e)
