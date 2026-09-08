# Take three numbers and check if they are in geometric progression.
a,b,c=map(int,input("Enter three numbers: ").split())
r1,r2=b/a,c/b
if r1==r2:
    print("Geometric progression")
else:
    print("Not a Geometric progression")