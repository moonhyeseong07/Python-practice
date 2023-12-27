age=int(input())
birth=2012-age+1

if(birth<2000):
    birth=str(birth)
    print(int(birth[2:4]),1)
else:
    birth=str(birth)
    print(int(birth[2:4]),3)
