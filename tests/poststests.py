import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 

import unittest, posts, post

class PostsTests(unittest.TestCase):
	def testPostInit(self):
		postDict = {"_id":99, "title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False}
		newPost = post.Post(postDict)
		self.assertIsNotNone(newPost)
		self.assertEqual(99, newPost._id)
		self.assertEqual("Test post", newPost.title)
		self.assertEqual("Content", newPost.content)
		self.assertEqual("Tags", newPost.tags)
		self.assertEqual("Added date", newPost.added)
	def testToHtml(self):
		postDict = {"_id":99, "title":"Test post", "content": "Content\n=======", "tags":"Tags", "added": "Added date", "archive":False}
		newPost = post.Post(postDict)
		html = newPost.toHtml()
		self.assertEqual(html, "<h1>Content</h1>")

class PostRepoTests(unittest.TestCase):
	def setUp(self):
		self.repo = posts.PostRepo()
	def tearDown(self):
		self.repo = None

	def testInsert(self):
		postDict = {"_id":99, "title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False} 
		self.repo.insert(postDict)
		postFound = self.repo.getById(postDict["_id"])
		self.assertIsNotNone(postFound)
		self.assertEqual(99, postFound._id)
		self.repo._delete(postDict["_id"])

if __name__ == '__main__':
    unittest.main()