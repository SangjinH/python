# 다양한 문제 상황이 존재 가능

# ================= 다익스트라 최단거리 알고리즘 ========================\
#
# 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.
# 매 상황에서 비용이 가장 적은 노드를 선택해 임의의 과정을 반복합니다.
# 그리디 알고리즘으로 분류

# 1. 출발 노드를 설정합니다.
# 2. 최단 거리 테이블을 초기화합니다.
# 3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택합니다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 위 과정에서 3, 4번을 반복합니다.

# 최단 거리 정보를 가지고 있는 상태에서 더 짧은 경로를 찾으면 더 짧은 거리로 갱신


# -------- 구현 방법
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().rstrip().split())
# 시작 노드를 입력받기
start = int(input().rstrip())
# 각 노드에 연결되어 있는 노드에 대한 정보를 입력받기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선의 정보 받기
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))  # a 번 노드에서 b번 노드로 가는 비용이 c라는 의미


# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드 (인덱스)
def get_smaller_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # 시작 노드에 대해서 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smaller_node()
        visited[now] = True
        # 현재 노드와 연결되 ㄴ다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(n + 1):
    # 도달할 수 없는 경우 , 무한 이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우
    else:
        print(distance[i])

# =================================================================
# 노드의 개수가 5000개 이하라면 위의 알고리즘으로 할 수 있지만,
# 노드의 개수가 10000개를 넘어가는 경우라면 ?

# ------------------ 우선순위 큐 ( Priority Queue )
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
# 우선순위 큐를 구현하기 위해 사용하는 자료구조는 힙 ( Heap )
# 최소 힙 ( Min Heap ) 과 최대 힙 ( Max Heap )이 있습니다.

import heapq


# 오름차순 힙 정렬 ( Heap Sort )
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# --------------------------------- 위의 다익스트라 알고리즘에서
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기위해
# Heap 자료구조를 이용
# 다익스트라 알고리즘이 동작하는 기본원리는 동일
# 가장 가까운 노드를 저장하기위해 힙 자료구조를 사용

# 개선된 구현 방법
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().rstrip().split())
# 시작 노드를 입력받기
start = int(input().rstrip())
# 각 노드에 연결되어 있는 노드에 대한 정보를 입력받기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선의 정보 받기
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))  # a 번 노드에서 b번 노드로 가는 비용이 c라는 의미


def update_dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
update_dijkstra(start)

## ------------------------- 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.

# 기본 점화식
# D_ab = min(D_ab*D_ak + D_kb)
