# 백준 1744 수묶기 , greedy
import sys
from collections import deque

input = sys.stdin.readline

nums = []
n = int(input().rstrip())

positives = []
negatives = []
zeros = []
total = []

for i in range(n):
    nums.append(int(input().rstrip()))
    if 0 < i:
        positives.append(i)
    elif i < 0:
        negatives.append(i)
    else:
        zeros.append(i)

positive_q = deque(positives)

if positive_q[0] == 1:
    total.append(positive_q.popleft())
else:
    while len(positive_q) < 2:
        a = positive_q.popleft()
        b = positive_q.popleft()
        total.append(a*b)

    if len(positive_q) == 1:
        total.append(positive_q.popleft())

if len(zeros) > 1 and len(negatives)


negative_q = deque(negatives)
while len(negative_q) < 2:
    a = negative_q.pop()
    b = negative_q.pop()
    total.append(a*b)
