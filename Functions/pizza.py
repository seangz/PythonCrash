def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for t in toppings:
        print("- " + t)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


