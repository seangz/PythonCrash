def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("(Enter q at anytime to quit) ")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

<<<<<<< HEAD
=======
def favorite_book(book):
	"""Favorite Books"""
	print("My favorite book is " + book.title())



favorite_book('the great gatsby')


def display_message():
	print("I'm learning about functions brah")

display_message()
>>>>>>> 5ca132270be588e1ae4abb0eccc6736a5943ab4f
