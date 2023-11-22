a, b = map(int, input().split())
print((("홀수" if a%2==1 else "짝수") + "+" + ("홀수" if b%2==1 else "짝수") + "=" + ("짝수" if (a+b)%2==0 else "홀수")))