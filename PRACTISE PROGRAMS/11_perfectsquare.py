# Check whether a number is a perfect square (without using the square root function)
num=int(input("Enter a number"))
for i in range(1,num):
    ans=i*i
    if ans==num:
        print(num,"is a perfect Square")
        break
else: print(num,"is not a perfect square")


