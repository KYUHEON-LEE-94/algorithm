array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 선택된 제일 앞의 원소.
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j #선택되었던 원소보다 작은 인덱스 값을 발견하면 값을 바꿔준다.
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)