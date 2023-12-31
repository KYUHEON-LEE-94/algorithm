def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v)
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
[],
[2,3,8], #1번노드와 연결된것
[1,7], #2번 노드와 연결된것
[1,4,5],
[3,5],
[7],
[2,6,8],
[1,7]
]

#각 노드가 발문된 정보를 표현(1차원 리스트)
    #0번째 인덱스는 사용하지 않는 방식으로 하기위한 *9
visited= [False] * 9
print(visited)

#정의된 DFS 함수 호출
dfs(graph, 1, visited);

