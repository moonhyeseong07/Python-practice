from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # node visited
    visited[start] = True

    # loop till queue is empty
    while queue:
        # visted node 'v' 
        v = queue.popleft()
        print(v, end=' ')

        # v 노드에 연결된 노드들 투입 -> 방문 안한 노드만 queue에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # print(queue) # queue안에 뭐있나
                visited[i] = True
