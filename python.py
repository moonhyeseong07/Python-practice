def recursive_sum(numbers):
    if not numbers:  # 리스트가 비어있으면 0을 반환
        return 0
    else:
        # 리스트의 마지막 요소를 꺼내서 더하고 재귀 호출을 수행
        last_number = numbers.pop()
        return last_number + recursive_sum(numbers)

# 숫자 리스트를 정의합니다.
numbers = [1, 2, 3, 4, 5]

# 재귀 함수를 호출하여 리스트의 모든 요소를 더합니다.
result = recursive_sum(numbers)

print(result)

