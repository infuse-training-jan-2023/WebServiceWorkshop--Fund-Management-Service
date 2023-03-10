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


@app.route('/loan', methods = ['POST'])
def add_loan_account():
	request_data = request.get_json()
	loan_amt = request_data['loan_amount']
	time_period = request_data['time_period']
	interest_rate = request_data['interest_rate']
	account_num = request_data['account_number']
	added_item = item_actions.add_loan_account(loan_amt, time_period, interest_rate, account_num)
	if added_item == {}:
		return Response("{'error': 'Error addding the item'}", mimetype='application/json', status=500)
	return Response(json.dumps(added_item), mimetype='application/json', status=201)


@app.route('/loan/<int:id>', methods = ['GET'])
def get_loan_account(id):
	item = item_actions.get_loan_account(id)
	if item == []:
		return Response("{'error': 'ID doesn't exist'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)


@app.route('/loans', methods = ['GET'])
def get_all_loan_accunts():
	items = item_actions.get_all_loan_accounts()
	return Response(json.dumps(items), mimetype='application/json', status=200)


@app.route('/loanSum', methods = ['GET'])
def get_all_loan_amount_sum():
	item = item_actions.get_all_loan_amount_sum()
	if item == []:
		return Response("{'error': 'No Loan Accounts found'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)


@app.route('/loanDeposit', methods = ['POST'])
def add_loan_deposit():
	request_data = request.get_json()
	deposit_amt = request_data['deposit_amount']
	loan_id = request_data['loan_ID']
	added_item = item_actions.add_loan_deposit(deposit_amt, loan_id)
	if added_item == {}:
		return Response("{'error': 'Error addding the item'}", mimetype='application/json', status=500)
	return Response(json.dumps(added_item), mimetype='application/json', status=201)


@app.route('/loanDepositSum', methods = ['GET'])
def get_all_loan_deposit_sum():
	item = item_actions.get_all_loan_deposit_sum()
	if item == []:
		return Response("{'error': 'No Loan Deposits found'}", mimetype='application/json', status=404)
	return Response(json.dumps(item), mimetype='application/json', status=200)


@app.route('/Account', methods = ['POST'])
def create_account():
    request_data = request.get_json()
    name = request_data["username"]
    email = request_data["emailID"]
    mobile = request_data["mobile_number"]
    city = request_data["city"]
    add_items = actions.create_account(name, email, mobile, city)
    if add_items == {}:
        return Response("{'error': 'Error adding the item'}", mimetype='application/json', status=500)
    return Response(json.dumps(add_items), mimetype='application/json', status = 201)


@app.route('/Account/<int:acc_num>', methods = ['GET'])
def get_account_details(acc_num):
    items = actions.get_account_details(acc_num)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)


@app.route('/Account', methods = ['GET'])
def get_all_account_details():
    items = actions.get_all_account_details()
    return Response(json.dumps(items), mimetype='application/json', status=200)


@app.route('/Deposit', methods = ['POST'])
def deposit_amount():
    request_data = request.get_json()
    acc_no = request_data["account_number"]
    amount = request_data["amount"]
    items = actions.deposit_amount(acc_no, amount)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)


@app.route('/Deposit/<int:acc_num>', methods = ['GET'])
def get_all_deposit_amount(acc_num):
    items = actions.get_deposit_amount(acc_num)
    return Response(json.dumps(items), mimetype='application/json', status=200)


@app.route('/Delete', methods = ['DELETE'])
def delete_user():
    request_data = request.get_json()
    acc_no = request_data["account_number"]
    items = actions.delete_user(acc_no)
    if items == {}:
        return Response("{'Error':'Account not Found'}", mimetype='application/json', status=404)
    return Response(json.dumps(items), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug = "True", port = 5000, host = '0.0.0.0')
