x=input()
if x.isalpha():
    print(invalid)
else:
    x=int(x)
    if x%4==0:
        print("yes")
    else:
        print("no")
