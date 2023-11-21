n = int(input())
total = 0

# 반복 조건을 변경하여 음수가 아닌 동안 반복하도록 수정합니다.
while n > 0:
    # 가장 큰 화폐 단위부터 계산하여 해당 화폐로 얼마나 사용할 수 있는지 확인합니다.
    if n >= 50000:
        total += n // 50000
        n %= 50000
    elif n >= 10000:
        total += n // 10000
        n %= 10000
    elif n >= 5000:
        total += n // 5000
        n %= 5000
    elif n >= 1000:
        total += n // 1000
        n %= 1000
    elif n >= 500:
        total += n // 500
        n %= 500
    elif n >= 100:
        total += n // 100
        n %= 100
    elif n >= 50:
        total += n // 50
        n %= 50
    elif n >= 10:
        total += n // 10
        n %= 10

# 결과 출력
print(total)
