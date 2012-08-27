class Validator:
	"""Validate form data"""
	def __init__(self):
		self.errors = {}
		self.submittedValues = {}
	def isValidPost(self, request):
		title = request.form["title"]
		content = request.form["content"]
		if title == "":
			self.errors["title"] = "Title cannot be empty"
		else:
			self.submittedValues["title"] = title
		if content == "":
			self.errors["content"] = "Content cannot be empty"
		else:
			self.submittedValues["content"] = content
		if len(self.errors) == 0:
			return True
		return False