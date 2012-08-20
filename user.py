class User:
	"User class for login"
	def __init__(self, username="andy", password="password"):
		self.username = username
		self.password = password
	def is_authenticated(self):
		if self.username == "andy":
			if self.password == "password":
				return True
		return False
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return unicode(999)
