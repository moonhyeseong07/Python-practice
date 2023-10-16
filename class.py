def countdown_num(n):
    if n <= 0:
        return 0
    else:
        print(n, '이(가) 양수인 경우!')
        result = countdown_num(n-1) + 1
        return result
print('반환값:',countdown_num(100))