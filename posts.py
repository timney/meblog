from pymongo import Connection
from datetime import datetime
import repobase, post, bson.objectid

class PostRepo(repobase.RepoBase):
	"post repository mongodb"

	def insert(self, postToAdd):
		posts = self.db.posts
		if postToAdd["tags"] == '':
			postToAdd["tags"] = []
		else:
			postToAdd["tags"] = postToAdd["tags"].strip().split(" ")
		post = { 
			"title": postToAdd["title"],
			"content" : postToAdd["content"],
			"tags" : postToAdd["tags"],
			"added" : datetime.utcnow(),
			"archive" : postToAdd["archive"]
		}
		if "_id" in postToAdd:
			if postToAdd["_id"] is not None or len(postToAdd["_id"]) > 0:
				post["_id"] = postToAdd["_id"]
		return posts.insert(post)

	def getById(self, id):
		posts = self.db.posts
		postFound = posts.find_one({"_id": bson.objectid.ObjectId(str(id)) })
		if postFound == None:
			return None
		else:
			return post.Post(postFound)

	def getAll(self):
		posts = self.db.posts
		postsAr = []
		for p in posts.find({ 'archive' : False}):
			postsAr.append(post.Post(p))
		return postsAr

	def update(self, postToUpdate):
		posts = self.db.posts
		post = { 
			"_id" : postToUpdate._id ,
			"title": postToUpdate.title,
			"content" : postToUpdate.content,
			"tags" : postToUpdate.tags,
			"added" : postToUpdate.added,
			"archive" : postToUpdate.archive
		}
		posts.update({ "_id": postToUpdate._id }, post)

	def _delete(self, id):
		post = self.db.posts
		post.remove(id) 