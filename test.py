while True:
    sentence=input().strip()
    if sentence=='#':
        break
    cnt=sum(1 for char in sentence if char.lower() in 'aeiou')
    print(cnt)