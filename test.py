def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers.pop() + recursive_sum(numbers)

def main():
    numbers = list(map(int, input().split()))
    result = recursive_sum(numbers)
    print(result)

if __name__ == "__main__":
    main()
