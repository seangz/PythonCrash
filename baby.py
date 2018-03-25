age = 13

if age < 2:
	person = ' baby'
elif age >= 2 and age < 4:
	person = ' toddler'
elif age >= 4 and age < 13:
	person = ' kid'
elif age >= 13 and age < 20:
	person = ' teenager'
else:
	person = 'n old AF human'



print("You are a" + person)