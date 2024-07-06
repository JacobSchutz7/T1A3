from student import Student
from assessment import Assessment
from data import *
from methods import *
from menu import menu

def main():
	while True:
		menu()
		choice = input("Choose task: ")
		
		match choice:
			case '1':
				add_students_from_file()
			case '2':
				add_assessment()
			case '3':
				mark_assessment()
			case '4':
				print("Exiting...")
				break
			case _:
				print("Invalid choice. Please try again.")

main()