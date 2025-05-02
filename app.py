from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite://messages.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'your-secret-key'

user_data = {}


actsuccess ={
	"Draw":"1111",
	"Chat":"1234",
	"See":"123"
}

messages=[]


@app.route('/localact', methods=['POST'])
def localact():
	print(request.method)
	data = request.get_json()
	user_id = data.get('user_id')
	act = data.get('act')
	password = data.get('password')
	if actsuccess.get(act) != password:
		return jsonify(success=False)
	
	user_data.setdefault(user_id,{})
	user_data[user_id][act] =True

	return jsonify(success=True)

@app.route('/post_message', methods=['POST'])
def post_message():
	data = request.get_json()
	messages.append({'username':data.get('username'),'text':data.get('text')})
	return jsonify({'status': 'ok'})

@app.route('/get_messages')
def	get_messages():
	return jsonify(messages)

@app.route('/')
def home():
	return render_template("test.html")

if __name__ == "__main__":
	app.run("0.0.0.0",port=5000)


