from flask import Flask, jsonify
import time
import threading


app = Flask(__name__)

def task(data):
	print("처리중")
	time.sleep(5)
	print("처리됨")

@app.route('/start/<task_id>')
def start(task_id):
	thread = threading.Thread(target=task, args=(task_id,))
	thread.start()
	return jsonify({"status": "started","tast_id":task_id})

@app.route('/')
def hoem():
	return "멀티 처리"

if __name__ == "__main__":
	app.run("0.0.0.0",5000)
