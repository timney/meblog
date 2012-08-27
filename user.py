class User:
	"User class for login"
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def is_authenticated(self):
		config = Configuration()
		if self.username == config.getUsername():
			if self.password == config.getPassword():
				return True
		return False
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return unicode(999)
