from flask import Flask, jsonify
from Scripts import sentiment as s

app = Flask(__name__)
@app.route("/")
def index():
	return jsonify({
		"data": "Success"
		})

@app.route("/tweet/<message>", methods=["GET", "PUT"])
def data(message):
	sent = s.sentiment(str(message))
	if sent[0] == "pos":
		return jsonify({
			"message" : message,
			"response": sent[1] * 100
			})
	elif sent[0] == "neg":
		return jsonify({
			"message" : message,
			"response": sent[1] * 100
			})


if __name__ == '__main__':
    app.run()