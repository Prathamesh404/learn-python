# Learn Regular Expressions.
|Expression |--Meaning--  |
|-----------|--------|
| **`^`**   | Matches the beginning of the line
| **`$`** | Matches the end of the line.
| **`.`** |  Matches any character.
| **`\s`** | Matches the whitespace characters.  
| **`\S`** | Matches the non-whitespace characters.  
| **`*`** | Repeats a character zero or more times.
| **`*?`** | Repeats a character zero or more times.(Non-Greedy)
| **`+`** | Repeats c character one or more times.
| **`+?`** -| Repeats c character one or more times.(Non-Greedy)
| **`[aeiou]`** | Matches a single character in the listed set.
| **`[^XYZ]`** | Matches a single character _not_ in the listed set.
| **`[a-z0-9]`** | The set of characters can include a range
| **`(`** | Indicates where string extraction is to start.
| **`)`** | Indicates where string extraction is to end.
|**`\d`**| Matches any decimal digit, this is equivalent to the class `[0-9]`
|**`\D`**| Matches any decimal digit, this is equivalent to the class `[^0-9]`
|**\w**| Matches any alphanumeric character; this is equivalent to class `[a-zA-Z0-9_]`
|**\W**| Matches any non-alphanumeric character; this is equivalent to class `[^a-zA-Z0-9_]`

### The Regular Expression Module.
`import re`
- `re.search()` - to see if the string matches the regular expression. Similar to find method for strings. It returns a `True/False` depending on whether string matches the regular expression.
- `re.findall()` - to extract portion of string that match your regular expression, similar to a combination of find() and slicing: `myVar[100:150]`


```Python
import re
x = "There are only 10 types of people: those who understand binary and those who don't, you 1 on them?"
y = re.findall('[0-9]+', x) # this [0-9] indicates One or more digits.
print(y)# ['10', '1']
# We get the list of all matches.
```
-------------------------------------
### Understanding Greedy v/s Non-Greedy.

- **Greedy Matching** : The repeat characters (`*` and `+`) push outward in both directions(greedy) to match the largest possible string.

```Python
import re
x = "From: all the things : this"
y = re.findall('^F.+:', x)
print(y) # ["From: all the things :"]
# It doesn't stop with first match, it continues till we find terminating term.
```
```Python
import re
x = "From: all the things : this"
y = re.findall('^F.+?:', x)
print(y) # ["From: "]
```
-------------------------------------
### Fine-Tuning String Extraction.
- We can refine the match for `re.findall()` and seperately determine which portion of the match is to be extracted by using the parentheses.

```Python
# Example 1
x = "From ronaldo@madrid.sp Sat Jan"
y = re.findall('\S+@\S+', x)
print(y) # ["ronaldo@madrid.sp"]

# Example 2
z = re.findall('^From (\S+@\S+)', x) # the explicit start from "From" helps to start from it, but only show the result between parentheses.
print(z) # ["ronaldo@madrid.sp"]

# Example 3
lin = re.findall('@([^ ]*)', x)
print(lin) # ["madrid.sp"]
```
