sum_price = int(input())
n = int(input())
result=0

for i in range(1,n+1):
    price,count = map(int,input().split())
    result+=price*count
    
if result==sum_price:
    print("Yes")
    
else:
    print("No")