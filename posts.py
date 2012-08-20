from pymongo import Connection
from datetime import datetime

class PostRepo:
	"post repository mongodb"
	def __init__(self):
		self.connection = Connection("mongodb://andy:at030884@dbh36.mongolab.com:27367/myblog")
		self.db = self.connection["myblog"]
	def insert(self, title, blog, tags):
		posts = self.db.posts
		post = { 
			"title":title,
			"blog" : blog,
			"tags" : tags.split(" "),
			"added" : datetime.utcnow()
		}
		return posts.insert(post)
	def getById(self, id):
		posts = self.db.posts
		return posts.find_one({"_id":id})
	def getAll(self):
		posts = self.db.posts
		postsAr = []
		for post in posts.find():
			postsAr.append(post)
		return postsAr