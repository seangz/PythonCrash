available_toppings = ['pepperoni','sausage','bacon','chicken']

requested_toppings = ['mushroom','sausage','green peppers']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping)
	else:
		print("We only serve meat!! No " + requested_topping.upper() + "!!!")

print("Finished making your pizza.")


