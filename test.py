n=int(input())
for i in range(0,n):
    if(i==0)or(i==n-1):
        for j in range(0,n):
            print("*",end='')
        print()
    else:
        print("*",end='')
        for j in range(0,n-2):
            print(' ',end='')
        print("*",end='')
        print()