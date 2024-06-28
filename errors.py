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

def validate_entry(prompt, dictionary, exists):
	try: 
		key = input(prompt)
		if (exists and key in dictionary) or (not exists and key not in dictionary):
			raise ValueError(f"Entry {'already' if exists else 'does not'} exist.")
		return key
	except ValueError as e:
		print(f"Error: {e}")