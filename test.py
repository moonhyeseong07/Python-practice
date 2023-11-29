n=int(input())
o_num = ''
if(n%10==1):
    o_num=str(n)+'st'
    if(n== 11):
        o_num=str(n)+'th'
elif(n % 10 == 2):
    o_num=str(n)+'nd'
    if(n==12):
        o_num=str(n)+'th'
elif(n%10==3):
    o_num=str(n)+'rd'
    if(n==13):
        o_num=str(n)+'th'
else:
    o_num=str(n)+'th'
print(o_num)