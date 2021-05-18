from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fcjbybxxybotbh:cea588c79eaceb5987ebedb8f74431cd94d6aefebe84200e4e35bcb38f0a4c44@ec2-52-45-73-150.compute-1.amazonaws.com:5432/d1mvsutcaqpo6n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
	return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quote_data = Favquotes(author=author, quote = quote)
	db.session.add(quote_data)
	db.session.commit()
	return redirect(url_for('index'))