# Rendering Templates

# Generating HTML from within Python is not fun, and actually pretty cumbersome
# because you have to do the HTML escaping on your own to keep the application secure.
# Because of that Flask configures the Jinja2 template engine for you automatically.

# To render a template you can use the render_template() method. All you have to do is
# provide the name of the template and the variables you want to pass to the template
# engine as keyword arguments. Here's a simple example of how to render a template:

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

# Flask will look for templates in the templates folder. So if your application is a module,
# this folder is next to that module, if it's a package it's actually inside your package:

# Case 1: a module:
# /application.py
# /templates
#	/hello.html

# Case 2: a package:
# /__init__.py
# /templates
#	/hello.html

# For templates you can use the full power of Jinja2 templates. Head over to the official
# Jinja2 Template Documentation for more information.

# Here is an example template:

<!doctype html>
<title>Hello from Flask</title>
{% if name %}
	<h1>Hello {{ name }}!</h1>
{% else %}
	<h1>Hello World!</h1>
{% endif %}

# Inside templates you also have access to the request, session, and g objects as well as
# the get_flashed_messages() function.

# Templates are especially useful if inheritance is used. If you want to know how that
# works, head over to the Template Inheritance pattern documentation. Basically
# template inheritance makes it possible to keep certain elements on each page (like
# header, navigation and footer).

# Automatic escaping is enabled, so if name contains HTML it will be escaped
# automatically. If you can trust a variable and you know that it will be safe HTML (for
# example because it came from a module that converts wiki markup to HTML) you can
# mark it as safe by using the Markup class or by using the |safe filter in the template.
# Head over to the Jinja2 documentation for more examples.

# Here is a basic introduction to how the Markup class works:

from flask import Markup
Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
Markup.escape('<blink>hacker</blink>')
# Markup(u'&lt;blink&gt;hacker&lt;/blink&gt')
Markup('<em>Marked up</em> &raquo; HTML').striptags()
u'Marked up \xbb HTML'