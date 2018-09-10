magicians = ['peter','david','john','smith']
thegreat = []

def show_magicians(magicians):
    while magicians:
        new_magicians = magicians.pop()
        print(new_magicians.title())

def make_great(magicians):
    while magicians:
        thegreat = magicians + " the Great"



make_great(magicians)
show_magicians(thegreat)