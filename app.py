from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import flask_login, validator, tags, markdown, config
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
from user import User
from posts import PostRepo
app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = "login"
SECRET_KEY = "boomdiggy2012"

app.config.from_object(__name__)

@login_manager.user_loader
def load_user(userid):
	configuration = config.Configuration()
	if unicode(configuration.getId()) ==  userid:
		return User(configuration.getUsername(), configuration.getPassword())
	else:
		return None

login_manager.setup_app(app)

@app.route('/')
def index():
	postrepo = PostRepo()
	allPosts =postrepo.getAll()
	tagsCloud = tags.Tags()
	return render_template('index.html', 
		viewmodel = { 
			"posts" : allPosts, 
			"tagcloud": tagsCloud.Cloud() 
		})

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		userl = User(request.form["username"], request.form["password"])
		if userl.is_authenticated():
			if login_user(userl):
				flash("Logged in successfully.")
				return redirect(request.args.get("next") or url_for("posts"))
		else:
			flash("Username/Password combination not recognized.")
			return redirect(url_for("login"))
	else:
		return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out!")
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
	if request.method == 'POST':
		valid = validator.Validator()
		if valid.isValidPost(request) == True:
			posts = PostRepo()
			posts.insert({
				"title": request.form["title"],
				"content": request.form["content"], 
				"tags": request.form["tags"],
				"archive": request.form["archive"]
				})
			return redirect(url_for('index'))
		else:
			tagsCloud = tags.Tags()
			return render_template(
				'new.html', 
				viewmodel = { 
					"tagcloud" : tagsCloud.Cloud(), 
					"errors" : valid.errors,
					"submittedValues" : valid.submittedValues
				})
	else:
		tagsCloud = tags.Tags()
		return render_template(
			'new.html', 
			viewmodel = { 
				"tagcloud" : tagsCloud.Cloud()
			 })

@app.route("/post/<postid>")
def post(postid):
	posts = PostRepo()
	post = posts.getById(postid)
	if post == None:
		return abort(404)
	else:
		return render_template("view.html", post = post)

@app.route("/posts")
@login_required
def posts():
	postsRepo = PostRepo()
	posts = postsRepo.getAllAndArchived()
	return render_template("posts.html", posts = posts)

@app.route("/tag/<tag>")
def tag(tag):
	posts = PostRepo()
	allPosts = posts.getAllByTag(tag)
	return render_template('index.html', 
		viewmodel = {
			"posts" : allPosts,
			"tagHeader" : tag
		})

if __name__ == '__main__':
    app.run(debug=True)
