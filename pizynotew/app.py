
from flask import Flask, render_template, url_for, request

from cryptp import encode, decode

pizy = Flask(__name__)

@pizy.route("/")
def index():
	note = request.form.get('note')
	return render_template('index.html', note=note)

@pizy.route("/<url>")
def handle_text(url):
	txt = decode(url)
	return render_template("note.html", note=txt)
	
if __name__ == '__main__':
	pizy.run(debug=True)