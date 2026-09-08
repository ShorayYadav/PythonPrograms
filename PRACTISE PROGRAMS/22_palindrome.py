# plaindrome
num=int(input("Enter a number: "))
temp=num
rev=0
while temp!=0:
    r=temp%10
    rev=rev*10+r
    temp//=10
if rev==num:
    print("Palindrome")
else:
    print("Not a palindrome")    