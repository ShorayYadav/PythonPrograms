# Take a 3-digit number and check if all digits are distinct
num=int(input("Enter 3 digit number"))
a=num//100
b=(num//10)%10
c=num%10
if a!=b and b!=c and c!=a:
    print("All are distinct")
else:
    print("similar")