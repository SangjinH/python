#================================= 최단경로 알고리즘
# 가장 짧은 경로를 찾는 알고리즘
# 다익스트라 최단경로 알고리즘
# 음의 간선이 없을 때 정상적으로 동작
# 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.

# 1. 출발노드를 설정합니다.
# 2. 최단 거리 테이블을 초기화합니다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다.
# 4. 해당 노드를 거치며 최단거리를 갱신

# 간단한 다익스트라 구현 방법
# 단계마다 방문하지 않은 노드 중에서 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 테이블의 모든 원소를 확인합니다.

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
distance = [INF] * (n+1)

# 모든 간선정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 아직 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 노드와 연결된 다른 노드를 확인
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를ㄹ 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한 (INFINITY) 라고 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])


#=========================================== 다익스트라 성능분석
# 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형탐색해야합니다.
# 따라서 전체시간 복잡도는 O(V^2) 입니다.
# 일반적으로 5000개 이하라면 이 코드로 해결가능합니다.
# 그러나 노드가 10,000개를 넘어가면 ?