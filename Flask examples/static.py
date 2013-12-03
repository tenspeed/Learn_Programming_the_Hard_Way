# Static Files
# Dynamic web applications also need static files. That's usually where the CSS and
# JavaScript files are coming from. Ideally your web server is configured to serve them for
# you, but during development Flask can do that as well. Just create a folder called static
# in your package or next to your module and it will be available at /static on the application.

# To generate URLs for static files, use the special 'static' endpoint name:

from flask import Flask
app = Flask(__name__)

url_for('static', filename='style.css')

# The file has to be stored on the filesystem as static/style.css