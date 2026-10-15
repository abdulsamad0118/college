#  Uppercase Lowercase Digit Or Special

c=input("Enter character: ")
if len(c)!=1:
     print("Enter one character")
elif c.isupper():
     print("Uppercase")
elif c.islower():
     print("Lowercase")
elif c.isdigit():
     print("Digit")
else:
     print("Special")
