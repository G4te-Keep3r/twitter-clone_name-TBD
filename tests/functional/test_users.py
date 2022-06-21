from project import create_app


def test_home_page():
	"""
	GIVEN a Flask application configured for testing
	WHEN the '/' page is requested (GET)
	THEN check that the response is valid
	"""
	flask_app = create_app()#'flask_test.cfg')

	# Create a test client using the Flask application configured for testing
	with flask_app.test_client() as test_client:
		response = test_client.get('/')
		assert response.status_code == 200
		assert b"twitter-clone_name-TBD" in response.data
		assert b"sub heading stuff goes here" in response.data
		assert b"..." in response.data
		assert b"idealy some sarcastic remark" in response.data
		assert b"(maybe a pile of feathers or something)" in response.data

def test_home_page_post():
	"""
	GIVEN a Flask application configured for testing
	WHEN the '/' page is is posted to (POST)
	THEN check that a '405' status code is returned
	"""
	flask_app = create_app()#'flask_test.cfg')

	# Create a test client using the Flask application configured for testing
	with flask_app.test_client() as test_client:
		response = test_client.post('/')
		assert response.status_code == 405
		assert b"twitter-clone_name-TBD" not in response.data
		assert b"sub heading stuff goes here" not in response.data
