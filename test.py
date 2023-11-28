h,m=map(int,input().split())
r=m-30
if r>=0:
    print(h,r)
else:
    if h==0:
        print(23,60+r)
    else:
        print(h-1,60+r)