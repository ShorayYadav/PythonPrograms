# Take two dates (day and month) and determine which one comes first in the calendar.
d1,m1=map(int,input("Enter 1st date and month").split())
d2,m2=map(int,input("Enter 2nd date and month").split())
if m1<m2:
    if d1<d2:
        print("date= ",d1,"month= ",m1,"comes first in calendar")
    else:
        print("date= ",d2,"month= ",m2,"comes first in calendar")
else:
    print("date= ",d2,"month= ",m2,"comes first in calendar")            
            
