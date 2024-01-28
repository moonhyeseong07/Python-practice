h,m=map(int,input().split())
time=int(input())
e_h=(h+(m+time)//60)%24
e_m=(m+time)%60
print(e_h,e_m)