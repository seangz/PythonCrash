pets = {
    'pet1': {
    'animal' : 'rabbit',
    'name' : 'goopy',
    'owner' : 'sean',
    },
    'pet2': {
    'animal' : 'dog',
    'name' : 'daisy',
    'owner' : 'chandran uncle',
    },
    'pet3':{
    'animal' : 'cat',
    'name' : 'blacky',
    'owner' : 'john',
    },

}

for pet, info in pets.items():
    print(info['name'].title() + " is " + info['owner'].title() + "'s " + info['animal'] + ".")
