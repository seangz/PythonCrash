people = {
	'stephen':{
	'first_name':'stephen',
	'last_name':'kalayil',
	'age':'34',
	'city':'Washington DC',
	},
	'sumit':{
	'first_name':'sumit',
	'last_name':'agarwal',
	'age':'32',
	'city':'Washington DC',
	},
	'kajal':{
	'first_name':'kajal',
	'last_name':'patel',
	'age':'31',
	'city':'New York City',
	}


}

for nickname, info in people.items() :
	print (info['first_name'].title() + " " + info['last_name'].title())
	print ("Lives in " + info['city'].title() + " and is " + info['age'] + " years old.")
