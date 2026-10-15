#  Vowel Or Consonant

c=input("Enter character: ").lower()
if c in "aeiou":
     print("Vowel")
elif c.isalpha():
     print("Consonant")
else:
     print("Not alphabet")
