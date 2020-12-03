def meter_converter(distance, measurement_from, measurement_to):
    meter_distance = round(distance / measurement_to * measurement_from, 2)
    return meter_distance



def unit_converter():
    units = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.914,
        'meters': 1,
        'miles': 1609.34,
        'kilometers': 1000,
        }

    while True:
        distance = float(input('What distance would you like to convert?  '))
        conversion_from = input('What unit of measurement is the distance?  ')
        conversion_to = input('What unit of measurement do you want to convert this to?  ')

        while not units[conversion_from]:
            print('Please enter an approved measurement type:  ')
            conversion_from = input('What unit of measurement is the distance?  ')
        else:
            convert = meter_converter(distance, units[conversion_from], units[conversion_to])
            print(f'There are {convert} {conversion_to} in {distance} {conversion_from}!')
            return

unit_converter()
