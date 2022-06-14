from app import app



def test_hello():
	response = app.test_client().get('/')

	assert response.status_code == 200
	#assert response.data == b'Hello, World!'
	assert b"why does everyone greet the world..." in response.data
	assert b"then just destroy it" in response.data
