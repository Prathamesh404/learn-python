# This program deals with calculating the number of Upper Case and Lower case Letters in a String.

def string_case(s):
    d = {"Upper_Case":0, "Lower_Case": 0} # A Dictionary to store values and count of string with case
    for charac in s:
        if charac.isupper():
            d["Upper_Case"] += 1 # Increment the count by one
        elif charac.islower():
            d["Lower_Case"] += 1
        else:
            pass # neglecting white spaces and special characters

    print("The original  string is: ", s)
    print("Number of Upper case characters: ", d["Upper_Case"])
    print("Number of Lower case characters: ", d["Lower_Case"])

string_case("All that Glitters is not Gold, it maybe another shiny object")
