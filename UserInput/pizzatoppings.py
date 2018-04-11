prompt = "\nWhat pizza toppings do you want? "
prompt += "\nSay 'done' when you're done with your toppings. "

message = ""
while message != 'done':
	message = input(prompt)

	if message != 'done':
		print(message)