word=input().strip()
po=[]
for i in range(len(word)):
    if word[i]=='t':
        po.append(str(i+1))
result=' '.join(po)
print(result)