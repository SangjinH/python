# https://www.acmicpc.net/problem/1697
# 백준 1697번 , BFS, DFS 숨바꼭질
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().rstrip().split())


collects = []
def bfs(start, target):
    collects.append([start])
    num = start
    temp_list = [start]
    while True:
        li = []
        for i in temp_list:
            a = i-1
            b = i+1
            c = i*2
            li.append(a)
            li.append(b)
            li.append(c)

        collects.append(li)
        temp_list = li
        if target in collects:
            break

bfs(n,k)
print(collects)