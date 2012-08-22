import ConfigParser

class Configuration:
	"""Reading configuration"""

	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')

	def getConnectionString(self):
		return self.config.get('mongodb', 'connection')