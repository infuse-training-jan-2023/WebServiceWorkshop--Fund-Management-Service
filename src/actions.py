from repository import Repository

class Actions:
    def __init__(self) -> None:
        self.item_repo = Repository()

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
                        'accountNum': item[0],
                        'userName': item[1],
                        'emailID': item[2],
                        'mobileNum': item[3],
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
                        'accountNum': item[0],
                        'userName': item[1],
                        'emailID': item[2],
                        'mobileNum': item[3],
                        'city': item[4],
                        'balance': item[5]
                    }
                )
            return res
        except Exception as e:
            print(e)
            return {}

    def deposite_amount(self, bank_acc_no,amount):
        try:
            item = self.item_repo.deposite_amount(bank_acc_no, amount)
            return item
        except Exception as e:
            print(e)
            return {}

    def get_deposite_amount(self, bank_acc_no):
        try:
            item = self.item_repo.get_deposite_amount(bank_acc_no)
            res = []
            res.append({"Account number": bank_acc_no})
            sum = 0

            for items in item:
                sum += items[1]
                res.append(
                    {
                        "depositID": items[0],
                        "depositAmount": items[1]
                    }
                )
            print(res)
            res.append({"Sum of Deposits": sum })
            return res
        except Exception as e:
            print(e)
            return {}
