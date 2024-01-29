import os
from flask import Flask, render_template, request
import chatbot as cb
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def get_response():
	message = request.form.get('message')

	if message != None:
		print(message)
		print(type(message))
	
		ints = cb.predict_class(message)

		intents = json.loads(open('intents.json').read())
		res = cb.get_response(ints, intents)
	
		return render_template('index.html', data = res)

	return render_template('index.html')
						
# main driver function
if __name__ == '__main__':
    app.run(debug=True)
