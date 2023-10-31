def palindrome(num):
    reversed_str = str(num)[::-1]
    total = num + int(reversed_str)
    if str(total) == str(total)[::-1]:
        return "yes"
    else:
        return "no"

n = int(input())

result = palindrome(n)
print(result)
