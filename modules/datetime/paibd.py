#! /usr/bin/env python3
import datetime

pai = datetime.date(1992, 5, 16)
print(pai)
print(pai.year)
print(pai.month)
print(pai.day)

# notice that default format is : yyyy-mm-dd
pai_became_pissed = datetime.date(2017, 2, 15)
pai_normalised = datetime.timedelta(500)
print(pai_became_pissed + pai_normalised)

