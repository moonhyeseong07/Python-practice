a=int(input())
while str(a)[-1] == '0':
    a//= 10
print(str(a)[::-1])
b=list(str(a))
for i in range(len(b)):
    b[i] = int(b[i])
print(sum(b))