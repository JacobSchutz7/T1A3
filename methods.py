from student import Student
from assessment import Assessment
from data import list_of_students
from csv import *

# method to manually add a student
def add_student():
	# ask user for the name of the student
	name = input("Enter name: ")
	# check if name contains only letters
	if name.isalpha != True:
		print("Numbers detected. Please enter a valid name.")
	# check if name is too long
	elif len(name) > 40:
		print("Name too long. Please enter a valid name.")
	# if no errors, appends a new student object to the list of students using the input.
	else:
		list_of_students.append(Student(name))

# add students from a csv file
def add_students_from_file(file_name):
	pass