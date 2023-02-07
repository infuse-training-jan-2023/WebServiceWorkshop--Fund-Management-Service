from repository import Repository

class Actions:
	def __init__(self) -> None:
		self.item_repo = Repository()


	def add_loan_account(self, loan_amt, time_period, interest_rate, account_num):
		try:
			loan_account = self.item_repo.add_loan_account(loan_amt, time_period, interest_rate, account_num)
			return loan_account
		except Exception as e:
			print(e)
			return {}


	def get_loan_account(self, id):
		try:
			item = self.item_repo.get_loan_account(id)
			res = []
			for x in item:
				res.append({
					'loan_ID': x[0],
					'loan_amount': x[1],
					'time_period': x[2],
					'interest_rate': x[3],
					'payback_amount': x[4],
					'amt_paid': x[5],
					'amt_remaining': x[6],
					'status': x[7],
					'account_number': x[8]
				})
			return res
		except Exception as e:
			print(e)
			return {}


	def get_all_loan_accounts(self):
		try:
			items = self.item_repo.get_all_loan_accounts()
			res = []
			for item in items:
				res.append({
					'loan_ID': item[0],
					'loan_amount': item[1],
					'time_period': item[2],
					'interest_rate': item[3],
					'payback_amount': item[4],
					'amt_paid': item[5],
					'amt_remaining': item[6],
					'status': item[7],
					'account_number': item[8]
				})
			return res
		except Exception as e:
			print(e)
			return {}


	def get_all_loan_amount_sum(self):
		try:
			item = self.item_repo.get_all_loan_amount_sum()
			res = []
			for x in item:
				res.append({
					'Sum of All Loan Amounts': x[0]
				})
			return res
		except Exception as e:
			print(e)
			return {}


	def add_loan_deposit(self, deposit_amt, loan_id):
		try:
			loan_deposit = self.item_repo.add_loan_deposit(deposit_amt, loan_id)
			return loan_deposit
		except Exception as e:
			print(e)
			return {}


	def get_all_loan_deposit_sum(self):
		try:
			item = self.item_repo.get_all_loan_deposit_sum()
			res = []
			for x in item:
				res.append({
					'Sum of All Deposit Amounts': x[0]
				})
			return res
		except Exception as e:
			print(e)
			return {}


	def create_account(self, name, email, mob, city):
		try:
			item = self.item_repo.create_account(name, email, mob, city)
			return item
		except Exception as e:
			print(e)
			return {}


	def get_account_details(self, bank_acc_no):
		try:
			items = self.item_repo.get_account_details(bank_acc_no)
			res = []
			for item in items:
				res.append(
					{
						'account_number': item[0],
						'username': item[1],
						'emailID': item[2],
						'mobile_number': item[3],
						'city': item[4],
						'balance': item[5]
					}
				)
			return res
		except Exception as e:
			print(e)
			return {}


	def get_all_account_details(self):
		try:
			items = self.item_repo.get_all_account_details()
			res = []
			for item in items:
				res.append(
					{
						'account_number': item[0],
						'username': item[1],
						'emailID': item[2],
						'mobile_number': item[3],
						'city': item[4],
						'balance': item[5]
					}
				)
			return res
		except Exception as e:
			print(e)
			return {}


	def deposit_amount(self, bank_acc_no,amount):
		try:
			item = self.item_repo.deposit_amount(bank_acc_no, amount)
			return item
		except Exception as e:
			print(e)
			return {}


	def get_deposit_amount(self, bank_acc_no):
		try:
			item = self.item_repo.get_deposit_amount(bank_acc_no)
			res = []
			res.append({"Account number": bank_acc_no})
			sum = 0

			for items in item:
				sum += items[1]
				res.append(
					{
						"deposit_ID": items[0],
						"deposit_amount": items[1]
					}
				)
			print(res)
			res.append({"Sum of Deposit": sum })
			return res
		except Exception as e:
			print(e)
			return {}


	def delete_user(self, bank_acc_no):
		try:
			deletig_user = self.item_repo.delete_user(bank_acc_no)
			return deletig_user
		except Exception as e:
			print(e)
			return{}
