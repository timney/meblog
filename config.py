import ConfigParser

class Configuration:
	"""Reading configuration"""

	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')

	def getConnectionString(self):
		return self.config.get('mongodb', 'connection')

	def getId(self):
		return self.config.get('credentials', 'id')
		
	def getUsername(self):
		return self.config.get('credentials', 'user')

	def getPassword(self):
		return self.config.get('credentials', 'pass')

	def getSecret(self):
		return self.config.get('flask-login', 'secret')