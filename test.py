x,y=map(int,input().split())
n=list(map(int,input().split()))
for num in n:
    if num<y:
        print(num,end=' ')