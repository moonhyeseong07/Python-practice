length=int(input())
num=list(map(int,input().split()))
result=0
for i in num:
    if i%5==0:
        result+=i
print(result)