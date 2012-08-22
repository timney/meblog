from flask import Flask, render_template, request, redirect, url_for
import flask_login, validator, tags
from user import User
from posts import PostRepo
app = Flask(__name__)

loginManager = flask_login.LoginManager()

@loginManager.user_loader
def load_user(userid):
	return user.User()

@app.route('/')
def index():
	postrepo = PostRepo()
	allPosts =postrepo.getAll()
	tagsCloud = tags.Tags()
	cloud = tagsCloud.Cloud()
	return render_template('index.html', viewmodel = { "posts" : allPosts, "tagcloud": cloud })

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		userl = User(request.form["username"], request.form["password"])
		if userl.is_authenticated():
			#flask_login.login_user(userl)
			return redirect(url_for('edit'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
	if request.method == 'POST':
		valid = validator.Validator()
		if valid.isValidPost(request) == True:
			posts = PostRepo()
			posts.insert({
				"title": request.form["title"],
				"content": request.form["content"], 
				"tags": request.form["tags"],
				"archive": False
				})
			return redirect(url_for('index'))
		else:
			return render_template('edit.html', errors = valid.errors)
	else:
		return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)
    loginManager.setup_app(app)