# https://www.acmicpc.net/problem/2665
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0,0])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr2[nx][ny] == 1:
                arr2[nx][ny] = arr2[x][y] + 1
                q.append((nx, ny))

    return arr[n-1][n-1]


n = int(input())
arr = []
for _ in range(n):
    info = input().rstrip()
    temp = []
    for i in info:
        temp.append(int(i))
    arr.append(temp)

blocks = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            blocks.append([i, j])

cnt = 1
while True:
    arr2 = copy.copy(arr)
    lists = list(combinations(blocks, cnt))

    results = []
    for i in lists:
        for j in i:
            arr2[j[0]][j[1]] = 1

        results.append(bfs())

    if max(results) > 1:
        print(cnt)
        break
