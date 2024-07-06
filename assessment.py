class Assessment:
	def __init__(self, name, weight):
		self.name = name
		self.marks = 0
		self.weight = weight

	def get_name(self):
		return self.name
	
	def get_marks(self):
		return self.marks
	
	def get_weight(self):
		return self.weight
	
	def set_title(self, title):
		self.title = title

	def set_marks(self, marks):
		self.marks = marks
	
	def set_weight(self, weight):
		self.weight = weight