#car = input("What type of rental would you like? ")

#print("Let me see if I can find you a " + car.title() + ".")


guests = input("How many guests will be dining with us today?")
guests = int(guests)

if guests >= 8:
    print("You'll have to wait for a few mins")
else:
    print("Your table is ready!")


number = input("Give me a number and I'll let you know if it is a multiple of ten ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten")
else:
    print("Nope")
