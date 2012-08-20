from pymongo import Connection
from datetime import datetime
import repobase

class PostRepo(repobase.RepoBase):
	"post repository mongodb"
	def insert(self, title, blog, tags):
		posts = self.db.posts
		if tags == '':
			tags = []
		else:
			tags = tags.split(" ")
		post = { 
			"title":title,
			"blog" : blog,
			"tags" : tags,
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