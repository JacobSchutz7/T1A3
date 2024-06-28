from classes import Classes
from data import *

# Add a student to the cohort. 
def add_student(name):
	count = len(students)
	students[count] = name

# Add a new class e.g. "History 101"
def add_class(title):
	list_of_classes[title] = (Classes(title))

# Print classes
def print_classes():
	for i in list_of_classes:
		print(list_of_classes[i].get_title())

# Add a student to a class 
def add_student_to_class(student_ID, class_title):
	student = students.get(student_ID)
	class_object = list_of_classes[class_title]
	class_object.students[student_ID] = student

# Remove a student from cohort
def remove_student(student_ID):
	students.pop(student_ID)

# Remove a student from a class
def remove_student_from_class(student_ID, class_title):
	class_object = list_of_classes[class_title]
	class_object.students.pop(student_ID)

# Print all students in a class
def print_students_in_class(class_title):
	print(list_of_classes.get(class_title).students)