from sqlalchemy import Table, Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relationship, Session

Base = declarative_base()

user_address = Table("user_address", Base.metadata,
					 Column("user_id", Integer, ForeignKey('user.id')),
					 Column("address_id", Integer, ForeignKey('address.id'))
					 )
##############################################################################
class User(Base):
	""""""

	__tablename__ = "user"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)
	address = relationship("Address", secondary=user_address, backref="user")

	#-------------------------------------------------------------------------
	def __init__(self, name, fullname, password):
		"""Constructor"""
		self.name = name
		self.fullname = fullname
		self.password = password

	def __repr__(self):
		return "<User('%s', '%s', '%s', '%s')>" % (self.id, self.name, self.fullname, self.password)

##############################################################################
class Address(Base):
	""""""

	__tablename__ = "address"
	id = Column(Integer, primary_key=True)
	email_address = Column(String, nullable=False, unique=True)
	#user_id = Column(Integer, ForeignKey('user.id'))

	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	#user = relationship(User, backref=backref('address', order_by=id))

	#-------------------------------------------------------------------------
	def __init__(self, email_address):
		"""Constructor"""
		self.email_address = email_address

	def __repr__(self):
		return "<Address('%s', '%s')>" % (self.id, self.email_address)

##############################################################################

# create a connection to a sqlite database
# turn echo on to see the auto-generated sqlite
engine = create_engine("sqlite:///tutorial3.db", echo=True)

# get a handle on the table object
#user_table = User.__tablename__
# get a handle on the metadata
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# add a single new user
mike_user = User("mike", "Mike Driscoll", "password")
todd_user = User("todd", "Todd Smith", "abacab")
mike_user.address = [Address(email_address="mike@gmail.com")]
sue_user = User("sue", "Sue Rivera", "itss")
sue_user.address = [Address(email_address="srivera@csub.edu"), Address(email_address="tsmith86@gmail.com")]
todd_user.address = [Address(email_address="tsmith86@gmail.com"), Address(email_address="srivera@csub.edu")]
session.add_all([mike_user, todd_user, sue_user])
session.commit()

user_results = session.query(User).all()
address_results = session.query(Address).all()
user_address_results = session.query(user_address).all()

#search_results = session.query(User, Address).filter(User.id == Address.user_id).filter(User.name == "sue").all()

print "\n\n"
print "User table: ", user_results
print "\n\n"
print "Address table: ", address_results
print "\n\n"
print "Association results: ", user_address_results
print "\n\n"
#print "Number of results: ", len(search_results)
#print "\n\n"
#print "First Result: ", search_results[0]
#print "\n\n"
#print "Second Result: ", search_results[1]
#print "\n\n"