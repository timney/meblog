class Validator:
	"""Validate form data"""
	def __init__(self):
		self.errors = {}
	def isValidPost(self, request):
		title = request.form["title"]
		blog = request.form["blog"]
		if title == "":
			self.errors["title"] = "Title cannot be empty"
		if blog == "":
			self.errors["blog"] = "Content cannot be empty"
		if len(self.errors) == 0:
			return True
		return False