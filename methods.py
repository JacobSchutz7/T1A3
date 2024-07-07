# this file contains all the methods for the program
# that do not belong to a class.

# library imports
import csv
import json
import statistics as stats
# file imports
from student import Student
from assessment import Assessment
from data import *

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
	# if no errors, append new student object to list of students using the input.
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
				# error handling for missing column.
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
			student.assessments[assessment_name] = (Assessment(assessment_name))

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
	if not does_student_ID_exist(student_ID):
		print(f"Student ID {student_ID} not found.")
		return
	# check if assessment exists.
	if not does_assessment_exist(assessment_name):
		print(f"Assessment '{assessment_name}' not found.")
		return
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
	dict_of_students[student_ID].assessments[assessment_name].set_marks(mark)

# a method to calculate the overall grade for all students
def calculate_grade():
	# iterate over all students
	for each in list_of_students:
		# set a variable in this layer so that it resets after each student
		grade = 0
		# iterate over each assessment for an individual student
		for assessment in each.assessments:
			grade += assessment.mark
		# assign the final grade
		each.set_grade(grade)

# a method to print out info for all students
def print_all_student_info():
	# iterate over full list of students.
	for student in list_of_students:
		# use f string to print all the info.
		print(f"Name: {student.get_name()} ID: {student.get_ID()} Grade: {student.get_grade()} ")
	print("The mean grade of the class is: " + mean_grade())

# a method to write student info to an external file
def write_report(file_name):
	# calculate grades before writing reports
	calculate_grade()
	# store data to be written in here.
	students_data = []
	# iterate over all students.
	for student in list_of_students:
		# store data for each individual student here.
		student_info = {
			"Name": student.get_name(),
			"ID": student.get_ID(),
			"Assessments": [
				{"Name": assessment.name, "Mark": assessment.get_marks()} for name, assessment in student.assessments.items()
			],
			"Grade": student.get_grade()
		}
		# add data for the individual student to the data for the whole cohort.
		students_data.append(student_info)
	# write to new file
	with open(file_name, "w") as file:
		json.dump(students_data, file, indent = 4)
	print(f"Student information has been written to {file_name}")

# a method to calculate the mean grade of the class
def mean_grade():
	# iterate over the students in the list and add their grades to a new list called grades.
	grades = []
	for student in list_of_students:
		grades.append(student.get_grade())
	# call the mean function from statistics module to calculate the mean.
	stats.mean(grades)