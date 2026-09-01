# append()
print("append()")
num=[10,20,30,40,50]
num.append(60)
print(num)

# extend()
print("\nextend()")
num=[10,20,30,40,50]
num.extend([60,70,80])
print(num)

# insert()
print("\ninsert()")
num=[10,20,30,40,50]
num.insert(1,100)
print(num)

# remove()
# it removes first occurence of an element
print("\nremove()")
num=[10,20,30,40,50]
num.remove(30)
print(num)

# pop()
print("\npop()")
num=[10,20,30,40,50]
x=num.pop()
print(x)
print(num)
y=num.pop(3)
print(y)
print(num)

# clear()
print("\nclear()")
num=[10,20,30,40,50]
num.clear()
print(num)

# index()
print("\nindex()")
num=[10,20,30,40,50]
num.index(50)
print(num)

# count()
print("\ncount()")
num=[10,40,30,40,50]
num.count(40)
print(num)

# sort()
print("\nsort()")
num=[7,8,3,1,2]
num.sort()
print(num)

# reverse()
print("\nreverse()")
num=[10,20,30,40,50]
num.reverse()
print(num)

# copy()
print("\ncopy()")
num=[10,20,30,40,50]
new_num=num.copy()
print(new_num)


# to sort a list in descending order
# it donot returns sorted list i mean it donot returns anything
list=[1,3,2]
list.sort(reverse=True)
print(list)