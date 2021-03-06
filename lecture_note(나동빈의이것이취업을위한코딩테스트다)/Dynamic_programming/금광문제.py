# N X M 크기의 금광이 있습니다. 각 칸에는 특정크기의 금이 있다.
# 채굴자는 맨 처음 열, 어느 행에서 출발하여
# 매번 오른쪽, 오른쪽 위, 오른쪽 아래 로 이동해 채굴합니다.
# 채굴자가 얻을 수 있는 금의 초대는 ?

# 테스트 케이스 (Test Case) 입력
for tc in range(int(input())):
    # 금광정보
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = array[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)