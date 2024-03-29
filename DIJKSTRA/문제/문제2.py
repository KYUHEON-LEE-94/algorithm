
INF = int(1e9) #무한
n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신 -> 자기 자신 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    #A <-> B 비용이 1이라고 설정
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())
print(f'{x}, {k}')

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)