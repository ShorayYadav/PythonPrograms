# Take a 3-digit number and check if the sum of the first and last digit equals the middle digit
num=int(input("Enter 3 digit number: "))
sum=(num//100)+(num%10)
if (num//10)%10==sum:
    print("YES")
else:
    print("NO")
