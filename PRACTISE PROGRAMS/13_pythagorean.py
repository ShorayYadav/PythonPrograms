


a,b,c=map(int,input("Enter two sides of a triangle and 3rd side must be greater than 2 :").split())
sum=(a**2)+(b**2)
if (c**2)==sum:
    print("It is a pythagorean triplet")
else:
    print("It is not a Pythagorean triplet")    