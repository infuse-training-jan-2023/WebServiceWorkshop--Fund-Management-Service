from flask import Flask, Response, request
from actions import Actions
from repository import Repository
import json

app = Flask(__name__)
item_actions = Actions()
item_repository = Repository()
actions = Actions()

@app.route('/', methods = ['GET'])
def welcome():
	return "Fund Management Service"

@app.route('/loan/add', methods = ['POST'])
def add_loan_account():
	request_data = request.get_json()
	loan_amt = request_data['loanAmt']
	time_period = request_data['timePeriod']
	interest_rate = request_data['interestRate']
	account_num = request_data['accountNum']
	added_item = item_actions.add_loan_account(loan_amt, time_period, interest_rate, account_num)
	if added_item == {}:
		return Response("{'error': 'Error addding the item'}", mimetype='application/json', status=500)
	return Response(json.dumps(added_item), mimetype='application/json', status=201)

@app.route('/loan/get/<int:id>', methods = ['GET'])
def get_loan_account(id):
	item = item_actions.get_loan_account(id)
	if item == []:
		return Response("{'error': 'ID doesn't exist'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)

@app.route('/loan/getall', methods = ['GET'])
def get_all_loan_accunts():
	items = item_actions.get_all_loan_accounts()
	return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/loan/getSum', methods = ['GET'])
def get_all_loan_ammount_sum():
	item = item_actions.get_all_loan_ammount_sum()
	if item == []:
		return Response("{'error': 'No Loan Accounts found'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)

@app.route('/loanDeposit/add', methods = ['POST'])
def add_loan_deposit():
	request_data = request.get_json()
	deposit_amt = request_data['depositAmount']
	loan_id = request_data['loanID']
	added_item = item_actions.add_loan_deposit(deposit_amt, loan_id)
	if added_item == {}:
		return Response("{'error': 'Error addding the item'}", mimetype='application/json', status=500)
	return Response(json.dumps(added_item), mimetype='application/json', status=201)

@app.route('/loanDeposit/getSum', methods = ['GET'])
def get_all_loan_deposit_sum():
	item = item_actions.get_all_loan_deposit_sum()
	if item == []:
		return Response("{'error': 'No Loan Deposits found'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)

@app.route('/Account/Add', methods = ['POST'])
def create_account():
    request_data = request.get_json()
    name = request_data["userName"]
    email = request_data["emailID"]
    mobile = request_data["mobileNum"]
    city = request_data["city"]
    add_items = actions.create_account(name, email, mobile, city)
    if add_items == {}:
        return Response("{'error': 'Error adding the item'}", mimetype='application/json', status=500)
    return Response(json.dumps(add_items), mimetype='application/json', status = 201)

@app.route('/Account/Get/<int:acc_num>', methods = ['GET'])
def get_account_details(acc_num):
    items = actions.get_account_details(acc_num)
    print(items)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/Account/All', methods = ['GET'])
def get_all_account_details():
    items = actions.get_all_account_details()
    print(items)
    return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/Deposit', methods = ['POST'])
def deposit_amount():
    request_data = request.get_json()
    acc_no = request_data["accountNum"]
    amount = request_data["amount"]
    items = actions.deposite_amount(acc_no, amount)
    print(items)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/Deposit/Get/<int:acc_num>', methods = ['GET'])
def get_all_deposit_amount(acc_num):
    items = actions.get_deposite_amount(acc_num)
    # print(items)
    return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/Delete', methods = ['POST'])
def delete_user():
    request_data = request.get_json()
    acc_no = request_data["accountNum"]
    items = actions.delete_user(acc_no)
    print(items)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug = "True", port = 5000, host = '0.0.0.0')
