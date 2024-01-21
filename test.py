start,last=input().split()
start=ord(start)
last=ord(last)
for i in range(start,last+1):
    print(chr(i),end=' ')