team = []

if team:
	for user in team:
		if user == 'peter':
			print("Hello VMware Specialist!")
		else:
			print("Hello " + user.title() + "!")
else:
	print("We need a squad")