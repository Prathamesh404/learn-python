#! /usr/bin/env python3

# Making a Dictionary.
player1 = {"team": "Argentina", "jersey_num": 10}
print(player1)

#Accessing Values.
print(player1["team"]) # "Argentina"
print(player1["jersey_num"]) # 10

# Getting Value with get()
player2 = {"team": "Spain" , "Position":"Midfielder","rank": 21}


player_team = player2.get("team")
player_rank = player2.get("rank")
print(player_team)
print(player_rank)


# Adding a New Key value pair.
player2["level"] = "legend"
player2["score"] = 97

print(player2)

# Changing the value
player1["team"] = "Portugal"
player1["jersey_num"] = 7
print(player1)

# Deleting a Key-Value Pair.

del player2["level"]
print(player2)


# looping throught the dictionaries.
designations = {
    "Priyanka": "Managing Director",
    "Raviraj Pishe": "Chief Financial Officer",
    "Meghna Bandelwar": "Product Designer",
    "Ashay Pathak": "Lead Developer"
}

# Show each person's designations and name
for name, post in designations.items():
    print(f"{name} is a '{post}' of the company")

# Show only designations: values()
for post in designations.values():
    print(f"One of them is {post}")

for name in designations.keys():
    print(f"That's {name}, one of our cool team player")


# Nesting - > A List of dictionaries.

# Storign dictionaries in the list.
team_players = []

# Make a nee player and add to the list.
player_one = {
    "Name": "Priyanka",
    "Role": "Managing Director",
    "Salary": 15000000
}
team_players.append(player_one)
player_two = {
    "Name": "Raviraj",
    "Role": "Chief Financial Officer",
    "Salary": 15000000
}
team_players.append(player_two)
player_three = {
    "Name": "Meghna",
    "Role": "Product Designer",
    "Salary": 14500000
}
team_players.append(player_three)
player_four = {
    "Name": "Ashay",
    "Role": "Lead Developer",
    "Salary": 13000000
}
team_players.append(player_four)

# print(team_players)


# Information ABout all Players.

for player_dict in team_players:
    for k, v in player_dict.items():
        print(f"{k} : {v}")
    print("\n")

# Store multiple languages for each person.
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)
