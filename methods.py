from student import Student
from assessment import Assessment
from data import *
import csv

# method to manually add a student.
def add_student():
	# ask user for the name of the student.
	name = input("Enter name: ")
	# check if name contains only letters.
	if name.isalpha != True:
		print("Numbers detected. Please enter a valid name.")
	# check if name is too long.
	elif len(name) > 40:
		print("Name too long. Please enter a valid name.")
	# if no errors, appends a new student object to the list of students using the input.
	else:
		list_of_students.append(Student(name))

# add students from a csv file.
def add_students_from_file():
	# get the file name from the user.
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

# a method to add all students in the list to a dictionary. This is for lookup purposes. 
def update_student_dict(dictionary):
	# clear the dictionary to avoid using any outdated data.
	dictionary.clear()
	# fill the dictionary with data from the list of students. 
	dictionary.update({student.ID: student for student in list_of_students})

# a method to check if a student exists using their ID.
def does_student_ID_exist(student_ID):
	# returns true or false if the ID is a key in the student dictionary
	return student_ID in dict_of_students

# method to remove a student from the student list. 
def remove_student():
	# get input for ID of student to be removed.
	remove_ID = int(input("Enter ID for student to be removd: "))
	# check if ID exists.
	if does_student_ID_exist(remove_ID) == True:
		# create a new list without the removed student and replace the old list.
		list_of_students = [student for student in list_of_students if student.ID != remove_ID]
		print(f"Student with ID {remove_ID} was removed.")
	else:
		# notify the user if the ID did not exist to begin with.
		print(f"Student with ID {remove_ID} was not found.")

def add_assessment():
	# get input for the name of the assessment.
	assessment_name = input("Enter assessment name: ")
	# check that the assessment name isn't too long. 
	if len(assessment_name) > 40:
		print("Assessment name too long. Please enter a valid assessment name.")
	else:
		# create a new Assessment object.
		new_assessment = Assessment(assessment_name)
		# add it to the list of assessment objects.
		list_of_assessments.append(new_assessment)
		# add the new instance of the new assessment to each student.
		for student in list_of_students:
			student.assessments[assessment_name] = (Assessment(new_assessment))

# a method for checking if an assessment exists.
def does_assessment_exist(assessment_name):
	for each in list_of_assessments:
		if each.get_name() == assessment_name:
			return True
	return False
	
def mark_assessment():
	# get input for which student to mark.
	student_ID = int(input("Enter student ID: "))
	# get input for which assessment to mark.
	assessment_name = input("Enter assessment name: ")
	# check the student_ID exists.
	if not does_student_ID_exist():
		print(f"Student ID {student_ID} not found.")
	# check if assessment exists.
	if not does_assessment_exist():
		print(f"Assessment '{assessment_name}' not found.")
	try:
		# get mark as user input.
		mark = int(input("Enter mark: "))
		# check if mark is valid
		if mark < 0 or mark > 100:
			print("Invalid mark. Must be an integer between 0 and 100.")
			return
	# error handling for value errors.
	except ValueError:
		print("Invalid input. Please enter an integer between 0 and 100.")
		return
	# add the mark to the specified assessment.
	dict_of_students[student_ID].assessment[assessment_name].set_marks(mark)