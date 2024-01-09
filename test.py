n=int(input())
numbers=list(map(int, input().split()))
result=0
for num in numbers:
    if num%2==1:
        result+=1
print(result)
