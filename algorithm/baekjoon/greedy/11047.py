import sys

n, k = map(int,input().split())

count = 0
coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
    if i > k:
        continue
    else:
        count += k//i
        k = k - i * (k//i)

    if k == 0 :
        break

print(count)