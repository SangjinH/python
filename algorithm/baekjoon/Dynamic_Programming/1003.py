# 백준 1003, 피보나치수열
import sys
input = sys.stdin.readline

global cnt_0
global cnt_1


def fibo(n):
    global cnt_0
    global cnt_1

    if n == 0:
        cnt_0 += 1
        return 0
    if n == 1:
        cnt_1 += 1
        return 1

    return fibo(n-1) + fibo(n-2)

num = int(input().rstrip())
result = []
for _ in range(num):
    cnt_0 = 0
    cnt_1 = 0
    fibo(int(input().rstrip()))
    result.append([cnt_0, cnt_1])

for i in range(len(result)):
    for j in range(2):
        print(result[i][j], end=' ')
    print()