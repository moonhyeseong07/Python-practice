def f_ball(M,swaps):
    ball_po=1
    for swap in swaps:
        x,y=swap
        if ball_po==x:
            ball_po=y
        elif ball_po==y:
            ball_po=x
    return ball_po
M=int(input())
swaps=[list(map(int,input().split()))for _ in range(M)]
print(f_ball(M,swaps)) 