""" to check if string is pallindrome"""

string1 = input("ENter a string to Reverse")
newstr= ""
string1=string1.lower()
for i in string1:
    newstr= i + newstr
print(newstr)
if string1==newstr:
    print("String is pallindrome")
else:
    print(" String is Not a pallindrome")


