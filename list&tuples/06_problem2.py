#WAP IN PYTHON WHETHER THE LIST INPUT BY USER IS PALINDROME OR NOT

l1=[1,2,3]
l2=[1,2,1]
copy_l1=l1.copy()
copy_l2=l2.copy()
copy_l1.reverse()
copy_l2.reverse()
if copy_l1==l1:
    print("List 1 is palindrome")
else:
    print("List 1 is not a palindrome")
if copy_l2==l2:
    print("List 2 is palindrome")
else:
    print("List 2 is not a palindrome")   
