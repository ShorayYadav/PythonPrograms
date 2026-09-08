# armstrong
num=int(input("Enter an integer: "))
count=0
while num!=0:
    num//=10
    count+=1
print(count)
temp=num
rev=0
while temp!=0:
    r=temp%10
    rev+=r**count
    temp//=10
if rev==num:
    print("Armstrong")
else:
    print("Not a Armstrong")    
