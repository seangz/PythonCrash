my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
friend_foods.append('bananas')
friend_foods.append('apples')


print("My favorite foods are")
for food in my_foods[0:1]:
	print(food)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nHere are the first 3 foods on my friends list")
for food in friend_foods[0:3  ]:
	print(food)