sandwiches = ['tuna','pastrami','italian','pastrami','cheesesteak','chicken','pastrami']
made = []

print("Looks like we are out of pastrami.")
sniwhile 'pastrami' in sandwiches:
	sandwiches.remove('pastrami')


while sandwiches:
	finished = sandwiches.pop()

	print("Made you a " + finished + " sandwich")

	made.append(finished)


print("We made all these sandwiches")

for sandwich in made:
	print("This " + sandwich + " sandwich is gonna be good") 