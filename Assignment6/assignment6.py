from flask import Flask,jsonify,request,make_response,url_for,redirect
import json

app = Flask(__name__)
my_data = {}

@app.route("/")
def main():
	return "Welcome to my Flask PAge"

@app.route("/add/", methods=["POST"])
def add():
	temp = json.loads(request.data.decode('utf-8'))
	try:
		if not isinstance(temp["id"], int):
			return "Key should be a integer"
		if not isinstance(temp["value"], str):
			return "Value should be a string"
	except:
		return "Please provide correct details"
	if temp["id"] not in my_data.keys():
		my_data[temp["id"]] = temp["value"]
	print(my_data)
	return "Added successfully"

@app.route("/list/", methods=["GET"])
def list():
	return jsonify(my_data)

if __name__=="__main__":
	app.run(debug=True , host="0.0.0.0",port=7000)