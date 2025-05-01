from flask import Flask, render_template, jsonify, request
import jwt, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

user_data = {}
actsuccess ={
	"Draw":"1111",
	"Chat":"1234",
	"See":"123"
}


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

@app.route('/')
def home():
	return render_template("page.html")

if __name__ == "__main__":
	app.run("0.0.0.0",port=5000)


