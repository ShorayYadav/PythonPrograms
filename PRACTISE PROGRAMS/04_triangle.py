# Take three sides and check if they form a valid triangle.
a,b,c=map(int,input("Enter three sides of a triangle").split())
sum=0
if a<b:
    if b<c:
        sum=a+b
        if sum>c:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")    
    else:
        sum=a+c
        if sum>b:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")    
else:
    sum=b+c
    if sum>a:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")            