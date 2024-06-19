f = open("input.txt", "r")
g = int(f.readline())
graph = [[0 for _ in range(g)] for _ in range(g)]
stack = []
visited = [False for _ in range(g)]
answer = []

while True :
    v = list(map(int, f.readline().split()))
    if not v :
        break
    graph[v[0]][v[1]] = 1
    graph[v[1]][v[0]] = 1

def dfs(n) :
    
    stack.append(n)
    
    while len(answer) != g :
        v = stack.pop()
        visited[v] = True
        answer.append(v + 1)
        
        for i in range(g-1, -1, -1) :
            if graph[v][i] and not visited[i] :
                stack.append(i)
    print(*answer)

dfs(0)