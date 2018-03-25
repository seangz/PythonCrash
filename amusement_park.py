age = 65

if age < 4:
	print("Your admission cost is $5")
elif age < 18:
	print("Your admission cost is $10")
else:
	print("Your admission cost is $20")


if age < 4:
	price = 5
elif age < 18:
	price = 10
elif age > 64:
	price = 5
else:
	price = 20

print("Your admission cost is $" + str(price))