# N개의 원소를 포함하는 수열이 오름차순으로 정렬되어 있을떄,
# 수열에서 x가 등장하는 횟수를 구하면 ?

from bisect import bisect_right,bisect_left

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, m = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, n, m)

if count == 0:
    print(-1)
else:
    print(count)