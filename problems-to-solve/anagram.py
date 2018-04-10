# This program deals with checking anagrams.
# Anagrams are two different words or sentences that contains same letters, arranged differently.
#Both can or cannot be legit statement.(Dictionary meaning, authencity isn't necessary)
# We basically check two strings.

# The Most easiest one.

def anagram_1(s1,s2):
    """
    This funtion take  two strings. Check them with same letters.
    and give output for True or False.
    """
    s1 = s1.replace(' ', '').lower()
    #replace method/lower method
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2) # using sorted method, it can be used for any iterable.

print(anagram_1('god', 'dog'))
