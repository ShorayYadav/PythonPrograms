# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
amt=int(input("Enter an amount"))
if(amt%2==0):
    print("The amount can be evenly divided into 2000, 500, and 100 currency notes")
    n2000=amt//2000
    amt%=2000
    n500=amt//500
    amt%=500
    n100=amt//100
    amt%=100
    print("2000 note :",n2000)
    print("500 note :",n500)
    print("100 note :",n100)
else:
    print("The amount cannot be divided into 2000, 500, and 100 currency notes")
# //  → "How many notes can I take?"
# %   → "How much money is left?"