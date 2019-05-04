from flask import Flask, jsonify
import Sentiment as s

api = Flask(__name__)


@api.route("/")
def index():
	return jsonify({
		"message": "Success",
		"direction":"Go to http://127.0.0.1:5000/data/<message> the add your message at the end"
		})

@api.route("/data/<message>", methods=["GET", "PUT"])
def data(message):
	a = s.sentiment(str(message))
	return jsonify({
		"message" : message,
		"description": "prediction is either 1 for positive or 0 for negative and the confidence value",
		"prediction":str(a[0]),
		"confidence":str(a[1] * 100)
		})

if __name__ == '__main__':
	api.run("0.0.0.0", port=5000)
