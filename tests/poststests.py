import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 

import unittest, posts, post

class PostsTests(unittest.TestCase):
	def testPostInit(self):
		postDict = {"_id":"99", "title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False}
		newPost = post.Post(postDict)
		self.assertIsNotNone(newPost)
		self.assertEqual("99", newPost._id)
		self.assertEqual("Test post", newPost.title)
		self.assertEqual("Content", newPost.content)
		self.assertEqual("Tags", newPost.tags)
		self.assertEqual("Added date", newPost.added)
	def testToHtml(self):
		postDict = {"_id":"99", "title":"Test post", "content": "Content\n=======", "tags":"Tags", "added": "Added date", "archive":False}
		newPost = post.Post(postDict)
		html = newPost.toHtml()
		self.assertEqual(html, "<h1>Content</h1>")

class PostRepoTests(unittest.TestCase):
	def setUp(self):
		self.repo = posts.PostRepo()
	def tearDown(self):
		self.repo = None

	def testInsert(self):
		postDict = {"title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False} 
		id = self.repo.insert(postDict)
		postFound = self.repo.getById(id)
		self.assertIsNotNone(postFound)
		self.assertEqual(id, postFound._id)
		self.repo._delete(id)

	def testUpdate(self):
		postDict = { "title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False} 
		id = self.repo.insert(postDict)
		postFound = self.repo.getById(id)
		postFound.content = "new content"
		self.repo.update(postFound)
		updatedPostFound = self.repo.getById(id)
		self.assertIsNotNone(updatedPostFound)
		self.assertEqual("new content", updatedPostFound.content)
		self.repo._delete(id)

	def testObjectId(self):
		postDict = { "title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False} 
		id = self.repo.insert(postDict)
		postFound = self.repo.getById(id)
		self.assertIsNotNone(postFound)
		self.assertEqual(id, postFound._id)
		self.repo._delete(id)

	def testGetAllByTag(self):
		postDict = {"title":"Test post", "content": "Content", "tags":"Tags", "added": "Added date", "archive":False} 
		id = self.repo.insert(postDict)
		postFound = self.repo.getById(id)

		posts = self.repo.getAllByTag("Tags")

		for i in posts:
			print str(i)

		self.assertIsNotNone(posts)
		self.assertEqual(1, len(posts))
		self.assertEqual(id, posts[0]._id)

		self.repo._delete(id)

if __name__ == '__main__':
    unittest.main()