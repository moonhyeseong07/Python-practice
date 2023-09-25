n = int(input())
s = [int(input()) for _ in range(n)]

def f(n, a = 2):    # 저장할 변수와 n 그리고 a에 기본으로 2를 가져온다
    dp[a] = max(dp[a-3]+s[a-1]+s[a], dp[a-2]+s[a])  # dp값과 s값을 더한값 비교
    if n>a:
        f(n, a+1)   # 재귀함수
    else:
        print(dp[-1])   # 출력

dp = [0] * (n)
if len(s) <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    f(n-1)