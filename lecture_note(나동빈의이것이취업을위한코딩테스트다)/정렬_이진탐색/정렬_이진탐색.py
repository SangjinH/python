#------------------------------------------정렬 알고리즘

# 정렬이란 데이터를 특정 기준에 따라 순서대로 나열하는 것을 말함

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)

