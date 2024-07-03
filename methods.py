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

# add students from a csv file.
def add_students_from_file(file_name):
	try:
		# open the file.
		with open(file_name, "r", newline="") as students_file:
			# create a student object for each entry in the csv file.
			for row in students_file:
				try:
					new_student = Student(name = row["name"])
					list_of_students.append(new_student)
				# error handling for missing column (or improper formatting).
				except KeyError as e:
					print(f"Missing '{e}' column.")
				# erro handling for other errors.
				except Exception as e:
					print(f"Error creating Student object: {e}")
	# error handling for invalid file name.
	except FileNotFoundError: 
		print(f"File {file_name} not found.")
	# erorr handling for reading errors.
	except IOError:
		print(f"Error reading file {file_name}")
	# error handling for other errors.
	except Exception as e:
		print(f"Error: {e}")