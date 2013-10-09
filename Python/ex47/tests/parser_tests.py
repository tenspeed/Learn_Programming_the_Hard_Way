from nose.tools import *
from ex47.parser import Sentence, ParserError
from ex47 import parser

def test_peek():
	assert_equal(parser.peek([]), None)
	assert_equal(parser.peek([('noun', 'bear'), ('verb', 'eat')]), 'noun')

def test_match():
	assert_equal(parser.match([], 'noun'), None)
	assert_equal(parser.match([('noun', 'bear'), ('verb', 'eat')], 'noun'), ('noun', 'bear'))
	assert_equal(parser.match([('noun', 'bear'), ('verb', 'eat')], 'verb'), None)

def test_skip():
	word_list = [('noun', 'bear'), ('verb', 'eat')]
	parser.skip(word_list, 'verb')
	assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat')])
	parser.skip(word_list, 'noun')
	assert_equal(word_list, [('verb', 'eat')])
	assert_equal(parser.skip([('noun', 'bear'), ('verb', 'eat')], 'noun'), None)
	assert_equal(parser.skip([('noun', 'bear'), ('verb', 'eat')], 'direction'), None)

def test_parse_verb():
	assert_equal(parser.parse_verb([('stop', 'on'), ('verb', 'eat')]), ('verb', 'eat'))
	assert_raises(ParserError, parser.parse_verb([('noun', 'bear')]))

def test_parse_object():
	assert_equal(parser.parse_object([('stop', 'on'), ('noun', 'bear')]), ('noun', 'bear'))
	assert_equal(parser.parse_object([('stop', 'on'), ('direction', 'north')]), ('direction', 'north'))
	assert_raises(ParserError, parser.parse_object([('verb', 'eat')]))

def test_parse_subject():
	a_sentence = parser.parse_subject([('verb', 'eat'), ('noun', 'princess')], ('noun', 'bear'))
	assert_equal(a_sentence.subject, 'bear')
	assert_equal(a_sentence.verb, 'eat')
	assert_equal(a_sentence.object, 'princess')

def test_parse_sentence():
	a_sentence = parser.parse_sentence([('stop', 'on'), ('noun', 'bear'), ('verb', 'eat'), ('direction', 'north')])
	assert_equal(a_sentence.subject, 'bear')
	assert_equal(a_sentence.verb, 'eat')
	assert_equal(a_sentence.object, 'north')

	a_sentence = parser.parse_sentence([('stop', 'on'), ('verb', 'eat'), ('direction', 'north')])
	assert_equal(a_sentence.subject, 'player')
	assert_equal(a_sentence.verb, 'eat')
	assert_equal(a_sentence.object, 'north')

	assert_raises(parser.parse_sentence([('direction', 'north'), ('noun', 'bear'), ('verb', 'eat')]))

def test_sentence():
	a_sentence = Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess'))
	assert_equal(a_sentence.subject, 'bear')
	assert_equal(a_sentence.verb, 'eat')
	assert_equal(a_sentence.object, 'princess')