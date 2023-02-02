from flask import Flask, Response, request
import json
from actions import Actions


app = Flask(__name__)
actions = Actions()

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

@app.route('/Deposit/Get', methods = ['POST'])
def get_all_deposit_amount():
    request_data = request.get_json()
    acc_no = request_data["accountNum"]
    items = actions.get_deposite_amount(acc_no)
    print(items)
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
