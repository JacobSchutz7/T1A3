from personnel import Personnel

class Student(Personnel):
	def __init__(self, name, ID=0000):
		super().__init__(name)
		self.ID = ID
		