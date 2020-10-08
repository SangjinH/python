# https://www.acmicpc.net/problem/1032
# 백준 1032번, 구현, 명령 프롬프트
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())


bigyo = input().rstrip()

texts = []
for _ in range(n-1):
    texts.append(input().rstrip())

result = []
for i in range(n-1):
    for j in range(len(texts[i])):
        if bigyo[j] != texts[i][j]:
            result.append("?")
            continue
        
