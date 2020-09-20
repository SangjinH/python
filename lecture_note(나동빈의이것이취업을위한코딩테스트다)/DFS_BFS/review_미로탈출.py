# N X M 크기의 미로에 갇혔습니다.
# 동빈이의 위치는 (1,1)이며  미로의 출구는 (N,M)의 위치에 존재하며
# 한 번에 한칸씩 이동할 수 있습니다.
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어있습니다.
# 동빈이가 탈출하기위해 움직여야하는 최소 칸의 개수는 ?
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

from collections import deque

def bfs(x,y):
    # 큐 (Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y =queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))