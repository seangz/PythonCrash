def city_country(city, country):
	citycountry = city + ", " + country
	return citycountry.title()

t_citycountry = city_country('dallas', 'texas')
print(t_citycountry)