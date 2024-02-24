n=int(input())
c_o=0
for i in range(1,n+1):
    c_o+=str(i)[-1].count('1')
print(c_o)