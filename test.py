str=input()
num=list(map(int,str.split()))
average=sum(num)/len(num)
print("{:.2f}".format(average))
