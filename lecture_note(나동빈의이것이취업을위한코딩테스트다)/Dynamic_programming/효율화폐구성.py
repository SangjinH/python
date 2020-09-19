# N가지 종류의 화폐가 있다.
# 최소한로 이용해서 그 가치의 합이 M원이 되도록하려고한다.
# 예로 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이
# 가장 최소한의 화폐 개수입니다.

# M원을 만들기 위한 최소한의 화폐개수를 출력하는 프로그램을 작성하세요

# a_i = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식 : 각 화폐 단위인 k 를 하나씩 확인하며
#          a_i-k를 만드는 방법이 존재하는 경우 a_i = min(a_i, a_i-k+1)
#          a_i-k를 만드는 방법이 존재하지 않는 경우 a_i = INF

n, m = map(int, input().split())

array = []
# N개의 화폐 단위 정보를 입력받기
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 (Dynamic Programming) 진행
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])