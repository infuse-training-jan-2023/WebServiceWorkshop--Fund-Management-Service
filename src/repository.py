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
            interest = (loan_amt * time_period * interest_rate) / 100
            payback_amount = loan_amt + interest
            insert_cursor = cursor.execute("INSERT INTO Loans (loan_amount, time_period, interest_rate, payback_amount, amt_paid, amt_remaining, status, account_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (loan_amt, time_period, interest_rate, payback_amount, 0, payback_amount, True, account_num))
            self.connection.commit()
            return{
                'loan_ID': insert_cursor.lastrowid,
                'loan_amount': loan_amt,
                'time_period': time_period,
                'interest_rate': interest_rate,
                'payback_amount': payback_amount,
                'amt_paid': 0,
                'amt_remaining': payback_amount,
                'status': 1,
                'account_number': account_num
            }
        except Exception as e:
            raise Exception("Error: ", e)


    def get_loan_account(self, id):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = cursor.execute("SELECT * FROM Loans WHERE loan_ID = " + str(id))
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
            row = cursor.execute("SELECT SUM(loan_amount) FROM Loans")
            return row
        except Exception as e:
            raise Exception("Error: ", e)
    
    def update_loan(self, amt_paid, amt_remaining, status, loan_id):
        self.connect_db()
        cursor = self.connection.cursor()
        if (amt_remaining <= 0):
            amt_remaining = 0
            status = self.status
        insert_cursor = cursor.execute("UPDATE Loans SET amt_paid = ?, amt_remaining = ?, status = ? WHERE loan_ID = ?", (amt_paid, amt_remaining, status, loan_id, ))
        self.connection.commit()
        return{
            'loanDepositID': insert_cursor.lastrowid,
            'loan_ID': loan_id
        }

    def add_loan_deposit(self,deposit_amt, loan_id):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = self.get_loan_account(loan_id)
            for x in row:
                status = x[7]
                amt_paid = x[5]
                amt_remaining = x[6]
            if status == 0:
                raise TypeError("Loan amount paid fully or Account doesn't exist")
            insert_cursor = cursor.execute("INSERT INTO LoanDeposits (deposit_amount, loan_ID) VALUES (?, ?)", (deposit_amt, loan_id))
            self.connection.commit()
            amt_paid += deposit_amt
            amt_remaining -= deposit_amt
            loan_deposit = self.update_loan(amt_paid, amt_remaining, status, loan_id)
            loan_deposit.update({'deposit_amount': deposit_amt})
            return loan_deposit
        except Exception as e:
            raise Exception("Error: ", e)


    def get_all_loan_deposit_sum(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            row = cursor.execute("SELECT SUM(deposit_amount) FROM LoanDeposits")
            return row
        except Exception as e:
            raise Exception("Error: ", e)


    def create_account(self,name, email, mob, city):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            insert_cursor = cursor.execute('INSERT INTO Accounts (username, emailID, mobile_number, city, balance) VALUES (?, ?, ?, ?, ?)',
            (name, email, mob, city, self.Balance))
            self.connection.commit()
            return{
                'account_number': insert_cursor.lastrowid,
                'username': name,
                'emailID': email,
                'mobile_number': mob,
                'city': city,
                'balance': self.Balance
            }
        except Exception as e:
            raise Exception('Error: ', e)


    def get_account_details(self,bank_acc_no):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute('select * from Accounts where status=true AND account_number=?',(bank_acc_no, ))
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
            fetch_cursor = cursor.execute('select balance from Accounts where account_number=?', (bank_acc_no, ))
            balance = fetch_cursor.fetchone()[0]
            update_balance =  balance + amount
            insert_cursor = cursor.execute('INSERT INTO Deposits (account_number, deposit_amount) VALUES(?, ?)',
            (bank_acc_no, amount))
            update_cursor = cursor.execute('UPDATE Accounts SET balance=? WHERE account_number=?', (update_balance, bank_acc_no, ))
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
            rows = cursor.execute('select * from Deposits where account_number=?', (bank_acc_no, ))
            return rows
        except Exception as e:
            raise Exception('Error: ', e)



    def delete_user(self, bank_acc_no):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            fetch_status = cursor.execute('select status from Accounts where account_number=?', (bank_acc_no, ))
            if fetch_status.fetchone()[0] == 0:
                raise TypeError("Account Dosen't Exist")
            rows = cursor.execute('UPDATE Accounts SET status=? WHERE account_number=?', (0, bank_acc_no, ))
            self.connection.commit()
            return{
                'Bank_Account_Number': bank_acc_no,
                'status': self.status
            }
        except Exception as e:
            raise Exception('Error: ', e)
