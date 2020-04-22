
# Accept a number as input
num = int(input("Enter a number between 1 & 10 (inclusive)"))

# Create a string to format the output 
# This is optional, typing the string out each time works too.)
output_str = "You will travel to {} next!"

# Decide the destination based on the number
if num >= 1 and num <= 3:
	print(output_str.format('Greece'))
elif num >= 4 and num <= 6:
	print(output_str.format('Thailand'))
elif num >= 7 and num <= 9:
	print(output_str.format('Switzerland'))
elif num == 10:
	print(output_str.format('France'))
else:
	print("Your choice is invalid.")