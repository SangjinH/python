# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

print(coins)