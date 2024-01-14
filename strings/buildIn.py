text="Python is dynamic programming language"
text2  = "    Hello With Python    "
str1 = "Hello"
str2 = "World"


#Concat the two strings
concat  = str1 + " " + str2
print("Conat the two strings : ",concat)

#Upper Case the string
upper = text.upper()
print("Upper Case : ", upper)

#Lower Case the string
lower = text.lower()
print("Lower Case : ", lower)

#length of the string
length = len(text)
print("Length of the string: ", length)

#replace the string
new_text = text.replace("dynamic", "great")
print("Replace the string: ",new_text)

#split the string
split = text.split(" ")
print("Split the string: ",split)

#strip the leading and trailing on string
strip = text.strip()
print("Strip the leading and trailing", strip)

#substring the string
substring = "dynamic"
if substring in text:
    print(substring, "is found in text")

#find() with the string
find = text.find("dynamic")
print("Yes, i found it at ", find)







