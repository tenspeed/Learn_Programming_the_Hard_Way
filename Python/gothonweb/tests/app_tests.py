from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from gothonweb.map import Room

def test_index():
	# check that we get a 404 on the / URL
	resp = app.request("/")
	assert_response(resp, status="200")

	# test our first GET request to /hello
	resp = app.request("/")
	assert_response(resp)

	# make sure default values work for the form
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")

	# test that we get expected values
	room = Room("test_room", "this is the test room")
	resp = app.request("/game", method="POST", room=room)
	assert_response(resp, contains="Zed")