import pymongo
from pymongo import MongoClient

class mongo:

	db = None
	collection = None

	def __init__(self, database_name, collection_name):
		client = MongoClient()
		self.db = client.database_name
		self.collection = self.db.collection_name

	def change_collection(self, collection_name):
		self.collection = self.db.collection_name

	def insert_one(self, post):
		post_id = self.collection.insert_one(post).inserted_id
		return post_id

	def find(self, filters=None):
		return self.collection.find(filters)

	def find_one(self, targetValues):
		return self.collection.find_one(targetValues)

	def authenticate(name = None, password = None, source = None, mechanism = 'DEFAULT', **kwargs):
		self.db.authenticate(name, password, source, mechanism, **kwargs)

	def dropDatabase(self):
		self.collection.dropDatabase()


