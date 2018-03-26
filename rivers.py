rivers = {
'nile' : 'egypt',
'amazon' : 'brazil',
'mississippi' : 'usa',
'ganges' : 'india',
'congo' : 'africa'
}

for river, country in sorted(rivers.items()):
	if country != 'usa':
		print("The " + river.title() + " River runs through " + country.title())
	else:
		print("The " + river.title() + " river runs through " + country.upper())
