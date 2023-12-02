menu=[0,400,340,170,100,70]
menu1, menu2=map(int,input().split())
c=menu[menu1]+menu[menu2]
if(c>500):
    print('angry')
else:
    print('no angry')