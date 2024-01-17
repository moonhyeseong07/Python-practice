# Memoization 초기화
d = [0] * 100

def fibo(x):
    # base case
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    # 점화식을 그대로 구현
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
