# This version doesn't ignore white spaces.
def is_palindrome(string):
    return string == string[::-1]


# The Version which ignores white space.We use replace()
# method on the String.

def is_palindrome_2(string):
    string_wo_space = string.replace(" ", "")
    return string_wo_space == string_wo_space[::-1]


