current_users = ['sean','peter','avinash','vijay','ronnie','randall']
new_users = ['vinh','eugene','eric','Sean','Randall']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Sorry " + new_user.title() + " is already in use, please select a different name")
	else:
		print(new_user.title() + " is available.")