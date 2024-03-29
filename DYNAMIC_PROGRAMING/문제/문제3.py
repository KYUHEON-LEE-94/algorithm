#정수 n,m을 입력받기
n,m = map(int, input().split())
#N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)
#DP 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        #j원을 만드는 최소 개수
        if d[j - array[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] + 1)

#계산된 결과를 출력
if d[m] == 10001:
    print(-1) #최종적으로 M원을 만드는 방법이 없는 경우
else:
    print(d[m])
    print(d[:m])

