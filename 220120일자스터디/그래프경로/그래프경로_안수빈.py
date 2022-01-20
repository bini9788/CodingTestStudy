# https://j-ungry.tistory.com/152

def dfs(s): 
    visit[s] = True           # 방문한 상태로 바꿔주기
    for i in graph[s]:        # 해당 노드의 간선 목록에 대해 반복문 실행
        if visit[i] == False: # 노드에 방문한 적 없으면 방문
            print(visit)
            dfs(i) 
            
T = int(input()) 
for test_case in range(1,T+1): 
    v,e = map(int,input().split())      # 노드 수, 간선 수
    graph = [[] for _ in range(v+1)]    # 해당 인덱스가 출발노드인 간선 리스트 만들기
    visit = [False for _ in range(v+1)] # 방문여부 리스트 만들기 
    
    for j in range(e): 
        a,b = map(int,input().split())  # 간선시작, 간선도착 
        graph[a].append(b)              # 각 노드별 간선들을 추가 
    print(graph)
    s,g = map(int,input().split())      # 출발노드와 최종도착노드 
    dfs(s) 
    result = 0 
    if visit[g]==True:                  # 최종 도착 노드가 방문 상태이면 해당 경로가 있다고 반환
        result = 1 
    print(f"#{test_case} {result}")

