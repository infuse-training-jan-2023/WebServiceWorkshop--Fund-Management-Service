import sqlite3

class Repository:
    DBPATH = './todo.db'
    Balance = 0

    @staticmethod
    def connect_db():
        return sqlite3.connect(Repository.DBPATH)


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
            rows = c.execute('select * from Accounts where accountNum=?',(bank_acc_no,))
            print("Rows Value: " ,rows)
            return rows
        except Exception as e:
            raise Exception('Error: ',e)

    @staticmethod
    def get_all_account_details():
        try:
            conn = Repository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from Accounts')
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


    # @staticmethod
    # def create_loan_acc(loan_given, time_period, ints_rate, bank_acc_no):
    #     try:
    #         conn = Repository.connect_db()
    #         c = conn.cursor()
    #         insert_cursor = c.execute('insert into loans (Loan_Amount, Time_Period, Interest_Rate, Bank Account Number) VALUES (?,?,?,?)',
    #         (loan_given, time_period, ints_rate, bank_acc_no))
    #         conn.commit()
    #         return
    #         {
    #             'Id': insert_cursor.lastrowid,
    #             'Loan_Amount': loan_given,
    #             'Time_Period': time_period,
    #             'Interest_Rate': ints_rate,
    #             'Bank Account Number': bank_acc_no
    #         }
    #     except Exception as e:
    #         raise Exception('Error: ', e)
