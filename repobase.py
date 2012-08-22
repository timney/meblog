from pymongo import Connection
import config

class RepoBase:
	"Base class for accessing pymongdb"
	config = config.Configuration()
	connection = Connection(config.getConnectionString())
	db = connection["myblog"]
	