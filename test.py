a,b=map(int,input().split())
if(a%b==0):
    print(str(b)+'*'+str(int(a/b))+'='+str(a))
elif(b%a==0):
    print(str(a)+'*'+str(int(b/a))+'='+str(b))
else:
    print('none')