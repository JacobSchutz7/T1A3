class Assessment:
	def __init__(self, title, max_marks, weight):
		self.title = title
		self.marks = 0
		self.max_marks = max_marks
		self.weight = weight

	def get_title(self):
		return self.title
	
	def get_marks(self):
		return self.marks
	
	def get_max_marks(self):
		return self.get_max_marks
	
	def get_weight(self):
		return self.weight
	
	def set_title(self, title):
		self.title = title

	def set_marks(self, marks):
		self.marks = marks
	
	def set_max_marks(self, max_marks):
		self.max_marks = max_marks
	
	def set_weight(self, weight):
		self.weight = weight