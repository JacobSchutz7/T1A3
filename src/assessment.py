# class definition for assessments
class Assessment:
	def __init__(self, name):
		self.name = name
		self.marks = 0
	# setters and getters for all attributes
	def get_name(self):
		return self.name
	
	def get_marks(self):
		return self.marks
	
	def set_title(self, title):
		self.title = title

	def set_marks(self, marks):
		self.marks = marks