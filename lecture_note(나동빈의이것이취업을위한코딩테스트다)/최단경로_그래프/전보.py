# # N 개의 도시가 있고
# # 어느 날, C 라는 도시에서 위급 상황이 발생했다.
# # 그래서 최대한 많은 도시로 메시지를 보내고자한다.
#
# import sys
#
# input = sys.stdin.readline
# from collections import deque
#
# n, m, c = map(int, input().rstrip().split())
#
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# for _ in range(m):
#     a, b, c = map(int, input().rstrip().split())
#     graph[a].append((b, c))
#
# q = deque([c])
# visited[c] = True
# cnt = 0
# time = 0
# while q:
#     v = q.popleft()
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i[0]]:
#             cnt += 1
#             time = max(time, i[1])
#             q.append(i[0])
#
# print(cnt, time)

# 위 까지 내 풀이

# ======================= 선생님 풀이 ===========================
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, start = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(start)

cnt = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)