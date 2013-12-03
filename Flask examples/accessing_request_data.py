# The Request Object
# The current request method is available by using the method attribute. To access form
# data (data transmitted in a POST or PUT request) you can use the form attribute. Here
# is a full example of the two attributes mentioned above:

from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username']),
					   request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	# the code below is executed if the request method
	# was GET or the credentials were Invalid
	return render_template('login.html', error=error)