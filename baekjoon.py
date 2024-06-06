word=input()
count=[0]*26

for i in word:
    count[ord(i)-97]+=1

print(*count)