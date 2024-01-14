# Regular Expressions for Text Processing:

# Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
# The re module in Python is used for working with regular expressions.
# Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.
# Examples of regex usage: matching emails, phone numbers, or extracting data from text.
# re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement.

import re

text = "The quick brown fox jumped over the lazy dog"
pattern = r"fox"

#regex search
search = re.search(pattern,text)
if search:
    print("Pattern found :",search.group())
else:
    print("Pattern not found")

#regex match
match = re.match(pattern,text)
if match:
    print("Match found :",match.group())
else:
    print("Match not found")

#regex replacement
replacement = "dog"
replace = re.sub(pattern,replacement,text)
print("Replace :",replace)

#regex split 
pattern2 = r" "
result = re.split(pattern2,text)
print("Split :",result)

#regex find all
findAll = re.findall(pattern, text)
# if findAll in result:
print("Find all :",findAll)
# else:
#     print("No found")

