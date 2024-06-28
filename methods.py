from classes import Classes
from data import *
from errors import *

# Add a student to the cohort. 
def add_student():
	first_name = get_valid_name("First name: ")
	last_name = get_valid_name("Last name: ")
	name = first_name + last_name
	count = len(students)
	students[count] = name

# Add a new class e.g. "History"
def add_class():
	title = validate_entry("Enter class: ", list_of_classes, 1)
	list_of_classes[title] = (Classes(title))

# Print classes
def print_classes():
	for i in list_of_classes:
		print(list_of_classes[i].get_title())

# Add a student to a class 
def add_student_to_class():
	student_ID = int(input("Enter Student ID: "))
	class_title = input("Enter class title: ")
	# Get student ID and check if that student exists
	validate_entry(student_ID, class_title)
	# Add student to the class if inputs have been successfully validated
	student = students.get(student_ID)
	class_object = list_of_classes[class_title]
	class_object.students[student_ID] = student

# Remove a student from cohort
def remove_student():
	student_ID = int(input("Enter student ID: "))
	validate_student_removal(student_ID)

# Remove a student from a class
def remove_student_from_class():
	try:
		student_ID = int(input("Enter student ID: "))
		class_title = input("Enter class title: ")
		if validate_entry(student_ID, class_title):
			class_object = list_of_classes[class_title]
			if student_ID in class_object.students:
				class_object.students.pop(student_ID)
			else: 
				print("Student not in found in class.")
		else: 
			print("Student not found in class.")
	except ValueError as e:
		print(f"Error: {e}")

# Print all students in a class
def print_students_in_class():
	try:
		class_title = input("Enter class title: ")
		if class_title in list_of_classes:
			print(list_of_classes.get(class_title).students)
		else:
			print("Class not found.")
	except Exception as e:
		print("Error: {e}")