x,y,z=input().split()
if x.isalpha() or y.isalpha() or z.isalpha():
    print("invalid")
else:
    x=int(x)
    y=int(y)
    z=int(z)
    if x>=y and x>=z:
        print(x)
    elif y>=x and y>=z:
        print(y)
    elif z>=x and z>=y:
        print(z)
