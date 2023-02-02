from flask import Flask, Response, request
from actions import Actions
from repository import Repository
import json

app = Flask(__name__)
item_actions = Actions()
item_repository = Repository()

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

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=5000)