from pymongo import Connection

class RepoBase:
	"Base class for accessing pymongdb"
	connection = Connection("mongodb://andy:at030884@dbh36.mongolab.com:27367/myblog")
	db = connection["myblog"]
	