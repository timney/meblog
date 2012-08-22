class Validator:
	"""Validate form data"""
	def __init__(self):
		self.errors = {}
	def isValidPost(self, request):
		title = request.form["title"]
		content = request.form["content"]
		if title == "":
			self.errors["title"] = "Title cannot be empty"
		if content == "":
			self.errors["content"] = "Content cannot be empty"
		if len(self.errors) == 0:
			return True
		return False