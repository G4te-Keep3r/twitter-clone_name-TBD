from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Posts
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
	# login code goes here
	email = request.form.get('email')
	password_plain = request.form.get('password')
	remember = True if request.form.get('remember') else False

	userSearch = User.query.filter_by(email=email).first()

	# check if the user actually exists
	# take the user-supplied password, hash it, and compare it to the hashed password in the database
	if not userSearch or not check_password_hash(userSearch.password, password_plain):
		flash('Please check your login details and try again.')
		return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

	# if the above check passes, then we know the user has the right credentials
	login_user(userSearch, remember=remember)

	return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
	return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
	# code to validate and add user to database goes here
	email = request.form.get('email')
	username = request.form.get('username')
	password_plain = request.form.get('password')

	user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

	if user: # if a user is found, we want to redirect back to signup page so user can try again
		flash('Email address already exists')
		return redirect(url_for('auth.signup'))

	# create a new user with the form data. Hash the password so the plaintext version isn't saved.
	new_user = User(email=email, username=username, password=generate_password_hash(password_plain, method='sha256'))

	# add the new user to the database
	db.session.add(new_user)
	db.session.commit()

	return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))








@auth.route('/makepost')
def makepost():
	return render_template('makepost.html')

@auth.route('/makepost', methods=['POST'])
def makepost_post():
	# code to validate and add post to database goes here  --->>>> validate...length?
	post = request.form.get('post')

	# create a new post with the form data
	new_post = Posts(post=post, user_id=current_user.id)

	# add the new post to the database
	db.session.add(new_post)
	db.session.commit()

	return redirect(url_for('main.profile'))



@auth.route('/editbio')
def editbio():
	return render_template('editbio.html', bio=current_user.biography)

@auth.route('/editbio', methods=['POST'])
def editbio_post():
	# code to validate and add post to database goes here  --->>>> validate...length?
	newbio = request.form.get('newbio')

	# create a new post with the form data
	#new_post = Posts(post=post, user_id=current_user.id)
	user = User.query.filter_by(username=current_user.username).first()
	user.biography = newbio
	db.session.commit()

	# add the new post to the database
	#db.session.add(new_post)
	#db.session.commit()

	return redirect(url_for('main.profile'))





