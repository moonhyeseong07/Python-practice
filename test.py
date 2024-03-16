cm,kg=map(float,input().split())
standard=(cm-100)*0.9
biman=(kg-standard)*100/standard
if biman<=10:
    print("정상")
elif biman>10 and biman<=20:
    print("과체중")
else:
    print("비만")