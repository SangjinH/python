###스택 구현 예제

### QUE (큐) 자료구조

# 먼저 들어 온 데이터가 먼저 나가는 형식 ( 선입선출 )
# 입구와 출구가 모두 뚫려있는 터널과 같은 형태

# 큐 (Queue) 구현을 위해 deque 라이브러리 사용

from collections import deque

#====================== 재귀의 예제 ( 팩토리얼 ! )

# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#
#     return n * factorial_recursive(n-1)
#
# print(factorial_recursive(5))


#========================== DFS_BFS ( Depth - First Search )
# 재귀와 반복문 둘 다 사용할 수 있다면 반복문을 사용
# 스택자료구조 사용,

# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.

# DFS_BFS 의 동작 예제는 깊이 우선 탐색이다.

#dfs 메서드 정의
# def dfs(graph, v, visitied):
#     #현재 노드를 방문처리
#     visitied[v]=True
#     print(v, end=' ')
#     # 현재노드와 연결된 다른 노드를 재귀적으로 방문
#
#     for i in graph[v]:
#         if not visitied[i]:
#             dfs(graph, i, visitied)
#
# # 각 노드가 연결된 정보를  표현 (2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [False] * 9
#
# # 정의된 DFS_BFS 함수 호출.
# dfs(graph, 1, visited)
#
#
# #---------------------------- BFS ------------------------------
# # 너비우선탐색, 가까운 노드부터 우선적으로 탐색하는 알고리즘
# # 큐 자료구조를 이용하며,
# # 1. 탐색 시작노드를 큐에 삽입하고 방문 처리를 합니다
# # 2.
#
#
# from collections import deque
#
# def bfs(graph, start, visited):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재노드를 방문처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end=' ')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# # 각 노드가 연결된 정보를 표현 (2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [False] * 9
#
# # 정의된 BFS 함수 호출
# bfs(graph, 1, visited)


#--------------------------------------------------------
# 문제) 음료수 얼려먹기
# N X M 얼음틀이 있습니다. 구멍이 뚫려 있는 부분은 0,
# 칸막이가 존재하는 부분은 1 로 표시됩니다.
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우
# 얼음 틀의 모양이 주어졌으 때 생성되는 총 아이스크림의 개수는 ?
# 4 X 5 틀에서는 총 3개가 생성됩니다.
# 00110
# 00011
# 11111
# 00000
