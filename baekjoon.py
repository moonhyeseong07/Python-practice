a,b=map(int,input().split())
array=[]
for i in range(1,a+1):
    if(a%i==0):
        array.append(i)

if(b<=len(array)):
    print(array[b-1])
else:
    print(0)
