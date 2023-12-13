a,b,c,d=map(int,input().split())
bit=a*b*c*d
byte=bit/8
kb=byte/1024
mb=kb/1024
print("%0.1f MB"%mb)