# Take time (hours and minutes) and print the smaller angle between the hour and minute hands
a,b=map(int,input("Enter no. of Hours and Minutes").split())
ah,am=(a+(b/60))*30,b*6
angle=abs(ah-am)
if angle>180:
    angle=360-angle

print(angle, "is the smaller angle")