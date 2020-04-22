
# Create list of enrolled students (use any names you like)
enrolled_students = ["Harry", "Ron", "Hermione"]

# Accept a student's name as input
student_name = input("Enter your name: ")

# Check if the student is enrolled
if student_name in enrolled_students:
	print("You will receive credit.")
else:
	print("You will not receive credit.")