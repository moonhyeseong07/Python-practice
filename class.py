n = int(input())  
num = list(map(int, input().split())) 
for i in range(n - 1, -1, -1):
    print(num[i], end=' ')
