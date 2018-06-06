#! /usr/bin/env python3

phone_book =[{"name": "Rahul", "Number": 9995767688},{"name": "Ramos", "Number": 3244890991}]

the_names = list(map(lambda name: name["name"], phone_book))
print(the_names)
the_numbers = list(map(lambda number: number["Number"], phone_book))
print(the_numbers)


