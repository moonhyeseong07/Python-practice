# 빈 리스트 p와 q를 생성합니다.
p = []
q = []

# 사용자로부터 3개의 정수를 입력받고 리스트 p에 저장합니다.
for i in range(3):
    a = int(input())
    p.append(a)

# 사용자로부터 2개의 정수를 입력받고 리스트 q에 저장합니다.
for i in range(2):
    a = int(input())
    q.append(a)

# 리스트 p와 q를 오름차순으로 정렬합니다.
p = sorted(p)
q = sorted(q)

# f 변수에 p와 q의 가장 작은 값들을 더합니다.
f = p[0] + q[0]

# f 값을 10으로 나눈 후 다시 f에 더합니다.
f = f + f / 10

# 결과를 출력합니다.
print(f)
