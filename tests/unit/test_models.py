from project.models import User, Posts
from werkzeug.security import generate_password_hash
 
def test_new_user():
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the email, hashed_password, authenticated, and role fields are defined correctly
	"""
	user = User(email='patkennedy79@gmail.com', username='testusername', password=generate_password_hash('FlaskIsAwesome', method='sha256'))
	assert user.email == 'patkennedy79@gmail.com'
	#assert user.hashed_password != 'FlaskIsAwesome' ---> currently for my content password is hashed. If plain test is involved it is declared differently (password_plain probably)
	assert user.password != 'FlaskIsAwesome'
	#assert not user.authenticated ---> handled by "from flask_login import LoginManager"
	#assert user.role == 'user' ---> do not have any user roles defined or implemented yet

def test_new_user():
	"""
	GIVEN a Post model
	WHEN a new Post is created
	THEN check the post, and user_id fields are defined correctly
	"""
	post = Posts(post='sample post', user_id=1)
	assert post.post == 'sample post'
	assert post.user_id == 1

