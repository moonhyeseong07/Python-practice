# 빈 2차원 리스트 d를 생성합니다. 이 리스트는 20x20 크기이며 모든 요소가 0으로 초기화됩니다.
d = []
for i in range(20):
    d.append([0] * 20)

# 사용자로부터 정수 n을 입력 받습니다.
n = int(input())

# n번 반복하는 루프를 시작합니다.
for i in range(n):
    # 사용자로부터 두 개의 입력값을 문자열로 받고, 공백을 기준으로 분리하여 x와 y 변수에 할당합니다.
    x, y = input().split()

    # 입력된 x와 y를 정수로 변환합니다.
    x = int(x)
    y = int(y)

    # 행과 열을 토글(toggle)합니다. (0은 1로, 1은 0으로 변경)
    for j in range(20):
        d[x][j] = 1 - d[x][j]
        d[j][y] = 1 - d[j][y]

# 업데이트된 행렬을 출력합니다.
for row in d:
    print(*row)
