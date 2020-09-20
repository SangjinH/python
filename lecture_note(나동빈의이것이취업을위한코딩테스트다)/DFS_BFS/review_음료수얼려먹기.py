# N X M 얼음틀이 있고
# 구멍 뚫린 부분은 0, 물이 채워져있는 부분은 1
# 얼음 틀 모양이 주어졌을 때 만들어지는 아이스크림의 개수는 ?

def dfs(x,y):
    if x <= -1 or x > n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0 :
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)