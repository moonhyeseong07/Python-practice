x=int(input())
y=int(input())
if x>0:
    if y>0:
        print("1")
    else:
        print("4")
else:
    if x<0:
        if y<0:
            print("3")
        else:
            print("2")