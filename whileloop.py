# Initialize a counter
count = 0

# Loop infinitely
while True:
	# Increment the counter
	count += 1
	print(f"Count is {count}")

	# Check if the counter has reached a certain value
	if count == 10:
		# If so, exit the loop
		break

# This will be executed after the loop exits
print("The loop has ended.")
