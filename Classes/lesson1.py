#Classes are fundamental tools in as=ny respectable programming languages,
#Python makes it easy to make and create classes.
# let's do it in a classic way.
import datetime

class User(object):
    """docstring for User, this class can be used to make different method"""
    def __init__(self, full_name, date_of_birth): # init method, initialization a.k.a "Constructor"
        """this method is called everytime we create a class. self is generally a reference to the new object that is being created."""
        self.name = full_name
        self.date_of_birth = date_of_birth #yyyymmdd

        #Extract first_name and last_name from full_name.
        name_pieces = full_name.split(" ") # split method is used to split the full name, here whhen it encounters space, and saves it into an array.
        self.first_name = name_pieces[0] #which is element at index 0 in an array due to split method
        self.last_name = name_pieces[-1] # here "-1" indiactes last value, but eventually a second value.

    def age(self):
        """Return the age of user in years."""
        today = datetime.date(2001, 4, 23)
        yyyy = int(self.date_of_birth[0:4])
        dd = int(self.date_of_birth[4:6])
        mm = int(self.date_of_birth[6:])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today -dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)ˆ

user = User("Bog ledger", "19560705")
print(user.age()) # we dont need self method.
