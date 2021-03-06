# N명의 병사가 무자위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력이 있습니다.
# 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다.
# 배치과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다.
# 그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶습니다.

# 가장 긴 증가하는 부분수열 문제.
# 예를들어 array = [4, 2, 5, 8, 4, 11, 15] 일때
# 이 수열의 가장 긴 증가하는 부분수열은 4, 5, 8, 11, 15

n = int(input())
array = list(map(int,input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 전환
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))