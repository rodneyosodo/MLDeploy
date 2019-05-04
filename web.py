from flask import Flask, request, render_template, jsonify
import Sentiment as s
app = Flask(__name__, template_folder="Web/templates", static_folder='Web/static',)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('text')
        # Make prediction

        pred = s.sentiment(data)
        if pred[0] == 1:
        	ans = "Positive"
        elif pred[0] == 0:
        	ans = "Negative"
        #print(pred)
        return render_template('index.html', sentiment=ans)
    return render_template('index.html', sentiment='')
    
if __name__ == '__main__':
	app.run("0.0.0.0", port=5000)

