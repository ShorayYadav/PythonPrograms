str1="abcdefghijklm"
str2="nopqrstuvwxyz"
char=input("Enter a Character").lower()
if char in str1:
    print(char," lies b/w a and m")
elif char in str2:
    print(char," lies b/w n and z")
else:
    print("dont lie anywhere")        