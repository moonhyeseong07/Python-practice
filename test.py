n=int(input())
numbers=list(map(int,input().split()))
find_num=int(input())
count=0
for num in numbers:
    if num==find_num:
        count+=1
print(count)
