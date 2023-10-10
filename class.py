# 사용자로부터 정수 n을 입력받습니다.
n = int(input())

# 사용자로부터 n개의 정수를 입력받고 리스트 a에 저장합니다.
a = list(map(int, input().split()))

# 리스트 a를 내림차순으로 정렬하여 리스트 b에 저장합니다.
b = sorted(a, reverse=True)

# 빈 딕셔너리 d를 생성합니다.
d = {}

# 리스트 b의 원소를 순회하면서 해당 원소가 처음 나타나는 위치를 저장합니다.
for i in range(n):
    if b[i] not in d:
        d[b[i]] = i + 1

# 리스트 a의 각 원소와 해당 원소가 처음 나타나는 위치를 출력합니다.
for i in range(n):
    print(a[i], d[a[i]])
