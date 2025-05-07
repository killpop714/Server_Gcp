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



messages=[]

#운영자용 로그인
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data.get("password")

    if password == "admin1234":  # 운영자 비밀번호
        token = jwt.encode({"role": "admin"},SECRET_KEY,algorithm="HS256")
        return jsonify(token=token)
    return jsonify(error="비밀번호 틀림"), 403

#시발롬
@app.route('/localact', methods=['POST'])
def localact():
	auth_header = request.headers.get("Authorization","")
	token = auth_header.replace("Bearer ","")

	try:
		decoded = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
		if decoded.get("role") != "admin":
			return jsonify(success=False,error="권한 없음"),403
	except Exception as e:
		return jsonify(success=False,error="토큰 인증 실패"),403


	data = request.get_json()
	user_id = data.get('user_id')
	act = data.get('act')

	if not user_id or not act:
		return jsonify(success=False,error="user_id 또는 act 누락"),400
	
	user_data.setdefault(user_id,{})[act] = True
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
	return render_template("test4.html")

if __name__ == "__main__":
	app.run("0.0.0.0",port=5000)


