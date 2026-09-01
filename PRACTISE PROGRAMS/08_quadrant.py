# Take coordinates (x, y) and determine which quadrant the point lies in
x,y=map(int,input("Enter X and Y coordinate: ").split())
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
else:
    print("On X-axis")
