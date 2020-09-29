# 백준 4796번 , 그리디

from collections import deque

x = 3
y = 1

q = deque([(x, y)])
print(q.popleft())