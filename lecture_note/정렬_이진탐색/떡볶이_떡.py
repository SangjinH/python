# 떡의 길이가 일정하지 않은 상태에서
# 절단기의 높이를 15cm 로 지정하면
# 19, 14, 10, 17인 떡은 차례대로
# 4   0   0   2 이다
# 손님은 총 6cm 만큼 가져간다.
# 손님이 왔을 때 요청한 길이가 M 일때,
# 절단기의 높이의 최대값은 ?

######### 범위가 크기 때문에 이진탐색을 이용할 수 있구나 유추!

# step 1. 가장 긴 떡의 길이의 절반으로 잘라보고
#         그 값을 기준으로 다시 연산
# step 2. 다시 한 번 step 1 을 수행한 후
#         길이 수정

