from data import *
from methods import *
from menu import menu
from utility import *

def main():
	# use a while loop to keep the program running until the users exits.
	while True:
		menu()
		choice = input("Choose task: ")
		# match-case allows the user to determine what functions the program will execute.
		match choice:
			case '1':
				add_students_from_file()
				update_student_dict(dict_of_students)
			case '2':
				add_assessment()
			case '3':
				mark_assessment()
			case '4':
				print_all_student_info()
			case '5':
				write_report()
			case '0':
				print("Exiting...")
				break
			case _:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()