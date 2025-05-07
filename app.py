from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import jwt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///messages.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'your-secret-key'

user_data = {}

SECRET_KEY="apx10_124_714"
allowd_token= set()

actsuccess ={
	"Draw":"1111",
	"Chat":"1234",
	"See":"123"
}

messages=[]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data.get("password")

    if password == "admin1234":  # 운영자 비밀번호
        token = jwt.encode({"role": "admin"},SECRET_KEY,algorithm="HS256")
        return jsonify(token=token)
    return jsonify(error="비밀번호 틀림"), 403


@app.route('/localact', methods=['POST'])
def localact():



	data = request.get_json()
	user_id = data.get('user_id')
	act = data.get('act')
	password = data.get('code')
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
	return render_template("test3.html")

if __name__ == "__main__":
	app.run("0.0.0.0",port=5000)


