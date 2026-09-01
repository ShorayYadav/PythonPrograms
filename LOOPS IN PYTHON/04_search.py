x=int(input("Enter number you want to search :"))
search=(1,4,16,9,25,36,49,64,81,100)
i,n=0,1
while i<len(search):
    if search[i]==x:
        print(x,"is at index",i)
        n=0    
    i+=1
if n==1:
    print("No. not found") 
           