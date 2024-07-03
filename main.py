from student import Student
from assessment import Assessment
from data import list_of_students
from methods import *

add_students_from_file()

for student in list_of_students:
	print(student.get_ID())