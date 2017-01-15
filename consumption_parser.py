import codecs

foods = []
drinks = []
def parse_consumption():
    f = codecs.open('consumption.txt', 'r', 'utf8')
    timeTo = 'foods'
    for line in f:
        try:
            line.strip()
            consumption = line.split('=')
            consumption_dict = {
                'name': consumption[0],
                'charge': float(consumption[1])
            }
            if timeTo == 'foods':
                foods.append(consumption_dict)
            elif timeTo == 'drinks':
                drinks.append(consumption_dict)
        except IndexError:
            timeTo = 'drinks'
    f.close()
