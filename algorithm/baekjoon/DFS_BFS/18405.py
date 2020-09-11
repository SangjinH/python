# # 경쟁적 전염
# import sys
# from collections import deque
#
# def bfs(x, y, k):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         print(nx,ny)
#
#
#         if nx < 1 or nx >= n or ny < 1 or ny >= n:
#             continue
#
#         if loc[nx][ny] == 0:
#             loc[nx][ny] = k
#
#
#
# n, k = map(int, input().split())
#
# loc = []
# for i in range(n):
#     loc.append(list(map(int,input().split())))
#
# s, x, y = map(int, input().split())
# virus = [x for x in range(1,k+1)]
#
# print(loc)
#
# # print(virus)
#
# dx = [ -1, 1, 0, 0 ]
# dy = [ 0, 0, -1, 1 ]
#
# for i in range(s):
#     for k in virus:
#         for y in range(n):
#             for z in range(n):
#                 bfs(y,z,k)
# print(loc)
# print(loc[x-1][y-1])