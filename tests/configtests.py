import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 

import unittest, config

class ConfigTests(unittest.TestCase):
	"""Tests man"""

	def setUp(self):
		self.config = config.Configuration()

	def tearDown(self):
		self.config = None

	def testGet(self):
		con = self.config.getConnectionString()
		self.assertIsNotNone(con)
		self.assertEqual("mongodb://andy:at030884@dbh36.mongolab.com:27367/myblog", con)

if __name__ == '__main__':
    unittest.main()