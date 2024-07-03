from student import Student
from assessment import Assessment
from data import list_of_students, list_of_assessments
import csv

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
def add_students_from_file():
	file_name = input("Enter file name: ")
	try:
		# open the file.
		with open(file_name, "r", newline="") as students_file:
			csv_reader = csv.DictReader(students_file)
			# create a student object for each entry in the csv file.
			for row in csv_reader:
				try:
					new_student = Student(name = row['Name'])
					list_of_students.append(new_student)
				# error handling for missing column (or improper formatting).
				except KeyError as e:
					print(f"Missing '{e}' column.")
				# error handling for other errors.
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

def add_assessment():
	# get input for the name of the assessment.
	assessment_name = input("Enter assessment name: ")
	# check that the assessment name isn't too long. 
	if len(assessment_name) > 40:
		print("Assessment name too long. Please enter a valid assessment name.")
	else:
		# create a new Assessment object
		new_assessment = Assessment(assessment_name)
		# add it to the list of assessment objects
		list_of_assessments.append(new_assessment)