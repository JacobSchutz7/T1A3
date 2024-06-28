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

# Add a new class e.g. "History 101"
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
	if student_ID not in students:
		print(f"Student ID '{student_ID}' not found.")
		return
	# Get class title and check if that class exists
	if class_title not in list_of_classes:
		print(f"class '{class_title}' not found.")
		return
	# Add student to the class if inputs have been successfully validated
	student = students.get(student_ID)
	class_object = list_of_classes[class_title]
	class_object.students[student_ID] = student

# Remove a student from cohort
def remove_student():
	student_ID = int(input("Enter student ID: "))
	try: 
		if student_ID in students:
			students.pop(student_ID)
			print("Student removed.")
	except KeyError:
		print(f"Error: Student ID {student_ID} not found.")

# Remove a student from a class
def remove_student_from_class(student_ID, class_title):
	class_object = list_of_classes[class_title]
	class_object.students.pop(student_ID)

# Print all students in a class
def print_students_in_class(class_title):
	print(list_of_classes.get(class_title).students)