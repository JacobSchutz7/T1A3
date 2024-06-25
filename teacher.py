from personnel import Personnel

class Teacher(Personnel):
	def __init__(self, name):
		super().__init__(name)
	
	def add_student_to_class(student, class_ID):
		class_ID.students.append(student.ID) 