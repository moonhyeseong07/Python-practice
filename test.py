#예를 5로 들게
n=int(input()); sum=0
for i in range(1, n+1):
    sum+=i
#for문을 돌려서 계산 예를 5라고 하면 1+2+3+4+5
for i in range(n):#5번 반복
    for j in range(i+1):#i=0일때 1번 1일때 2번 반복
        print(sum, end=' ')# 공백으로 벌려서 출력
        sum-=1#sum을 빼줌
    print('')#줄바꿈