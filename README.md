# T1A3

## Link to Source Control Repository
[Link to my GitHub repo.](https://github.com/JacobSchutz7/T1A3)

## Code Style Guide
For this project I used the PEP 8 - Style Guide for Python Code found [here.](https://peps.python.org/pep-0008/)
## Feature List & Walkthrough
- The 'main' function:
This function contains a while loop that runs the program until the user chooses to exit. Within this loop, the 'menu' function is called to display options to the user. The user chooses what they want to do by inputting a number. A match-case statement then determines the next step. 
- Adding Students:
If the user inputs 1 to the main function, the 'add_students_from_file' function is called. This function reads the CSV file input by the user (students.csv is the provided file but another can be used if placed in the data_files folder). From this file, 'Student' objects are created and appends them to 'list_of_students'. This function also updates the student dictionary. This is maintained for easier lookup in certain situations. 
- Adding Assessment:
If the user inputs 2 to the main function, the 'add_assessment' function is called. This prompts the user for the name of the assessment. Functions to validate the input are called and then a new 'Assessment' object is created and added to each student objects Assessment attribute (which is a dictionary that uses the assessment name as a key and the assessment object itself as the value). 
- Marking Assessments:
If the user inputs 3 into the main function, the 'mark_assessment' function is called. This prompts the user for student ID and the assessment name. These inputs are then validated and then the user is prompted for the mark that is then added to the specified assessment for the specifised student. 
- Print Student Information: 
If the user inputs 4 into the main function, the 'print_all_student_info' function is called. The programs iterates over the list_of_students list and prints each students name, ID and grade. If the students have sufficient grade values then the mean grade of all the students is also calculated and displayed. 
- Writing Reports: 
If the user inputs 5 into the main function, the 'write_report' function. This function writes student info, including name, ID, grade and marks for each assessment, to a JSON file called report.json
- Exit
If the user inputs 0 into the main function the program will exit. 
## Implementation
[Link](https://trello.com/invite/b/88xowRSz/ATTIb9d2e315dd1e934bad02822780fd247d584AEC7E/t1a3) to my Trello board for this project.
The features on the trello board do not match the features in the project because I had to reduce the scope of the program late in development. It was a lot more complicated than it needed to be so features are almost the same but not quite as expansive as initially planned. 
## Help
### System requirements: 
- Python version 3.10.9 or higher
- OS: macOS or Linux (I don't have a windows machine so I have not tested it)
- Hardware: a working computer with a keyboard and screen.
### Installation: 
- The program is simple. No installation process is required. Simply download the files, navigate to ./T1A3/src/dist and run 'main' (./main) to start the program. 
### User Guide:
Upon launching the program the user will see the following menu: 
Gradebook Management System:
1. Import Students
2. Add Assessment
3. Mark Assessment
4. Print Student Info
5. Write Report
<ol start ="0">
	<li>Exit</li>
</ol>

#### Options
1. Import Students: to import students from a CSV file type '1' and press enter. You will then be prompted for the file name (students.csv is provided, you can edit this file or provide your own but it must be of suitable formatting). Type it in and press enter. The program will read the CSV file and add it to the system. If the file name is invalid or cannot be found an error will be raised. 
2. Add Assessment: to add an assessment type '2' and press enter. You will be prompted for the name of the assessment e.g., 'Research Essay'. Type the name and press enter. The program will create the assessment and add it to each student in the system. 
3. Mark Assessment: to mark an assessment type '3' and press enter. You will then be prompted to enter a student ID, then the name of the assessment, and the mark. Press enter after each. The program will assign the mark to the specified assessment for the specified student. 
4. Print Student Info: to print basic info for all students (name, ID, grade) type '4' and press enter. The program will print the information for each student in the system. 
5. Write Report: to write student information to an external file, type '5' and press enter. The program will write all student information including name, ID, grade and marks for each individual assessment to a json file named report.json
<ol start ="0">
	<li>To exit the program type '0' and press enter.</li>
</ol>

It is advised that you use these features in the order they are listed. 