from flask import Flask
app = Flask(__name__)

username = "tsmith"
post_id = 1

@app.route('/')
def index():
	return "Index Page"

@app.route('/hello')
def hello_world():
	return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return "User %s" % username

# the 'int' in <int:post_id> is a converter
# the following converters exist: int, float, path (like the default but also accepts slashes)
@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return "Post %d" % post_id

# These two rules look similar but behave differently.
# In the first case, the canonical URL for the projects endpoint has a trailing
# slash. In that sense, it is similar to a folder on a file system. Accessing it without a
# trailing slash will cause Flask to redirect to the canonical URL with the trailing slash.

# In the second case, however, the URL is defined without a trailing slash, rather like the
# pathname of a file on UNIX-like systems. Accessing the URL with a trailing slash will
# produce a 404 "Not Found" error.

# This behavior allows relative URLs to continue working even if the trailing slash is
# ommited, consistent with how Apache and other servers work. Also, the URLs will stay
# unique, which helps search engines avoid indexing the same page twice.
@app.route('/projects/')
def projects():
	return "The project page"

@app.route('/about')
def about():
	return "The about page"



if __name__ == '__main__':
	app.run(debug=True)