def compare(a,b,c,d):
    fraction1=a/b
    fraction2=c/d

    if fraction1>fraction2:
        print(">")
    elif fraction1==fraction2:
        print("=")
    else:
        print("<")

a,b,c,d=map(int,input().split())
compare(a,b,c,d)