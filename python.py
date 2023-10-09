k, n = map(int, input().split())
r = k // n + k % n
m = k // n
while r >= n:
    m = m + r // n
    r = r % n + r // n
print(m)