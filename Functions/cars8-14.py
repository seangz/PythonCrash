def car(manufacturer, model, **char):
    car2 = {}
    car2['manufacturer'] = manufacturer
    car2['model'] = model
    for key, value in char.items():
        car2[key]=value
    return car2


prelude = car('honda','prelude',year = 2000, color = 'black', mileage = 200000)

print(prelude)