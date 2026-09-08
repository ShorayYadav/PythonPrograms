# Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.
num=int(input("Enter an integer (1-9999): "))
temp,count,sum=num,0,0
while temp!=0:
    sum+=(temp%10)
    temp/=10
if sum>num:
    print("YES")
else:
    print("NO")        