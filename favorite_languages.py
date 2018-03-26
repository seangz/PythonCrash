favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}

for n, l in favorite_languages.items():
	print("\n" + n.title() + "'s favorite languages are:")
	for a in l:
		print("\t" + a.title())
