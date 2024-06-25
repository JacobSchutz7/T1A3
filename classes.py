class Classes:
	def __init__(self, title, ID, assessments, students=[]):
		self.title = title
		self.ID = ID
		self.assessments = assessments
		self.students = students
	
	def get_ID(self):
		return self.ID
	
	def get_students(self):
		return self.students