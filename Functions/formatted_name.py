<<<<<<< HEAD
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name ('sutharson','gnanarajah','sean')
print(musician)
=======
def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')

print(musician)
>>>>>>> 5ca132270be588e1ae4abb0eccc6736a5943ab4f
