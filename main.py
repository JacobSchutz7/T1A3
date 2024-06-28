from methods import *
from classes import Classes
from data import *
import csv

print("Welcome to Gradebook Manager!")

with open('students.csv', 'r') as student_list:
	csv_reader = csv.DictReader(student_list)
	for row in csv_reader:
		student_id = row['ID']
		name = row['Name']
		students[int(student_id)] = {'Name': name}

for key, value in students.items():
	print(key, value)