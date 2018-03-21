pizzas = ['pepperoni', 'onion','sausage']
friends_pizzas = pizzas[:]


for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really love pizza!")

pizzas.append('mushroom')
friends_pizzas.append('bacon')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's are:")
for pizza in friends_pizzas:
	print(pizza)