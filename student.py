class Student:
	def __init__(self, name):
		self.name = name
		self.ID = 0
		self.grade = 0
		self.assessments = []
	
	def get_name(self):
		return self.name
	
	def get_ID(self):
		return self.ID
	
	def get_grade(self):
		return self.grade
	
	def set_name(self, name):
		self.name = name
	
	def set_ID(self, ID):
		self.ID = ID
	
	def set_grade(self, grade):
		self.grade = grade	