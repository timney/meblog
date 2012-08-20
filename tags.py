from bson.code import Code
import repobase

class Tags(repobase.RepoBase):
	"""Map reduce tags stuff"""
	def Cloud(self):
		map =Code("function () {"
			"  this.tags.forEach(function(z) {"
			"    emit(z, 1);"
			"  });"
			"}")
		reduce = Code("function (key, values) {"
			"  var total = 0;"
			"  for (var i = 0; i < values.length; i++) {"
			"    total += values[i];"
			"  }"
			"  return total;"
			"}")
		result = self.db.posts.map_reduce(map, reduce, "myresults")
		return result.find()