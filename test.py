n = int(input())
numbers = list(map(int, input().split()))
find_num = int(input())

count = numbers.count(find_num)

print(count)
