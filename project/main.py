from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import Posts, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
	#return "teststring"
	#posts = Posts.query.order_by(Posts.id).all()[::-1]
	#posts = Posts.query.join(User, Posts.user_id==User.id).order_by(Posts.id).all()[::-1]
	#posts = Posts.query.join(User).order_by(Posts.id).all()[::-1]

	posts = db.session.query(Posts, User).filter(Posts.user_id == User.id).order_by(Posts.id).all()[::-1]

	return render_template('index.html', posts=posts)

@main.route('/profile')
@login_required
def profile():
	#reversed(session.query(User).order_by(User.id.desc()).limit(3).all())
	#posts = reversed(Posts.query(Posts).order_by(Posts.id.desc()).all()) #this is bad as it loads ALLL "tweets", but that is something to optimize later. Also currently its gonna show ALL tweets, not dynamic loading or pages of tweets. This is POC stage so its fine.
	
	#posts = reversed(Posts.query.order_by(id.desc()).all())
	#posts = reversed(Posts.query.order_by(Posts.id).all())
	#posts = Posts.query.join(User, User.id == Posts.user_id).filter_by(user_id=current_user.id).order_by(Posts.id).all()[::-1]
	#posts = db.session.query(Posts).filter_by(user_id=current_user.id).order_by(Posts.id).all()[::-1]
	
	#posts = Posts.query.filter_by(user_id=current_user.id).join(User, Posts.user_id==User.id).order_by(Posts.id).all()[::-1]
	posts = db.session.query(Posts, User).filter_by(user_id=current_user.id).filter(Posts.user_id == User.id).order_by(Posts.id).all()[::-1]

	#posts = db.session.query(Posts, User.id).join(User, User.id == Posts.user_id).filter_by(user_id=current_user.id).order_by(Posts.id).all()[::-1]
	#if len(posts) > 0:
	#	posts = reversed(posts)
	#reversed(Posts.query.all())

	#Posts.query(Posts).order_by(Posts.id.desc())
	#Posts.query(Posts).order_by(Posts.id.desc())
	#emailSearch = User.query.filter_by(email=email).first()
	#User.query.get(int(user_id))


	return render_template('profile.html', username=current_user.username, posts=posts, bio=current_user.biography)



	#tasks = Todo.query.order_by(Todo.date_created).all() #could use .first() to get newest here too (for some other use)
	#return render_template('index.html', tasks=tasks)
