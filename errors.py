from data import *

# Helper function for error handling
def get_valid_name(prompt):
	while True:
		try: 
			name = input(prompt)
			if not name.isalpa():
				raise ValueError("Numbers detected. Please input a valid name.")
			return name
		except ValueError as e:
			print(f"Error: {e}")

def validate_entry(student_ID, class_title):
	# Get student ID and check if that student exists
	if student_ID not in students:
		print(f"Student ID '{student_ID}' not found.")
		return False
	# Get class title and check if that class exists
	if class_title not in list_of_classes:
		print(f"class '{class_title}' not found.")
		return False
	return True

def validate_student_removal(student_ID):
	try: 
		if student_ID in students:
			students.pop(student_ID)
			print("Student removed.")
	except KeyError:
		print(f"Error: Student ID {student_ID} not found.")

