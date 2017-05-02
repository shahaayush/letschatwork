from flask import Flask, render_template, request, redirect, url_for
from models import *

app= Flask(__name__)




@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/')
def home():
	return render_template('home.html', posts=Post.select().order_by(Post.date.desc()))


@app.route('/new_post/')
def new_post():
	return render_template('new_post.html')

@app.route('/create/', methods=['POST'])
def create_post():
	Post.create(
		title= request.form['title'],
		text= request.form['text'].decode("utf-8")
	)
	
	return redirect(url_for('home'))

@app.route('/delete?id=<id>', methods=['POST'])

def delete_post(id):
	tria = Post.get(Post.id==id)
	tria.delete_instance()
	return redirect(url_for('home'))


#@deleting_post

if __name__== '__main__':
	app.run(debug=True)
	
