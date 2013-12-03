# HTTP knows different methods for accessing URLs. By default, a route only
# answers to GET requests, but that can be changed by providing the methods
# argument to the route() decorator. Here are some examples:

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

# If GET is present, HEAD will be added automatically for you. You don't have to deal
# with that. It will also make sure that HEAD requests are handled as the HTTP RFC
# (the document describing the HTTP protocol) demands, so you can completely ignore that
# part of the HTTP specification. Likewise, as of Flask 0.6, OPTIONS is implemented for
# you automatically as well.

# What are HTTP methods? The HTTP method (also often called "the verb") tells the server what the clients wants
# to do with the requested page. The following methods are very common:

# GET
# The browser tells the server to just get the information stored on that page and send it.
# This is probably the most common method.

# HEAD
# The browser tells the server to get the information, but it is only interested in the
# headers, not the content of the page. An application is supposed to handle that as if
# a GET request was received but to not deliver the actual content. In Flask you don't
# have to deal with that at all, the underlying Werkzeug library handles that for you.

# POST
# The browser tells the server that it wants to post some new information to that URL
# and that the server must ensure the data is stored and only stored once. This is how
# HTML forms usually transmit data to the server.

# PUT
# Similar to POST but the server might trigger the store procedure multiple times by
# overwriting the old values more than once. Now you might be asking why this is
# useful, but there are some good reasons to do it this way. Consider that the
# connection is lost during transmission: in this situation a system between the
# browser and the server might receive the request safely a second time without
# breaking things. With POST that would not be possible because it must only be
# triggered once.

# DELETE
# Remove the information at the given location.

# OPTIONS
# Provides a quick way for a client to figure out which methods are supported by this URL.
# Starting with Flask 0.6, this is implemented for you automatically.

# Now the interesting part is that in HTML4 and XHTML1, the only methods a form can
# submit to the server are GET and POST. But with JavaScript and future HTML
# standards you can use the other methods as well. Furthermore HTTP has become quite
# popular lately and browsers are no longer the only clients that are using HTTP. For
# instance, many revision control systems use it.