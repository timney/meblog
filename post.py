import markdown

class Post:
	"""Post model"""

	def __init__(self, post):
		self._id = post["_id"]
		self.title = post["title"]
		self.content = post["content"]
		self.tags = post["tags"]
		self.added = post["added"]
		self.archive = post["archive"]
		
	def toHtml(self):
		return markdown.markdown(self.content)

