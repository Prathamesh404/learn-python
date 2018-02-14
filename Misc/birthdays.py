birthdays = {"Ashwini":"Jan 5", "Prathamesh": "Feb 15", "Raviraj": "Feb 17","Priyanka": "April 26" }

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I don't have birthday information for " + name)
        print("What's their birthday")
        bday = input()
        birthdays[name] = bday
        print("Data updated for the Birthdays")
