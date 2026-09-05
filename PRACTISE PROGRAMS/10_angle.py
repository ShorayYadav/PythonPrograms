# Take two angles of a triangle and compute the third angle
a1,a2=map(int,input("Enter 2 angles of a triangle").split())
a3=180-(a1+a2)
print("Third Angle is :",a3)