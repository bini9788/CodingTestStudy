result =[]
T = int(input()) # 테스트 케이스 수
for test_case in range(1,T+1): 
    N,M = map(int,input().split()) # 정수개수, 구간수
    ai = list(map(int,input().split())) # 정수리스트
    sum_list=[] # 구간별 정수합 리스트
    for i in range(N):
        if ((i+M) <= N) & (len(ai[i:i+M]) == M): # 슬라이싱할때 인덱스 범위를 벗어나지 않도록 설정, 슬라이싱한 개수가 구간 개수와 동일한지 확인
            sum_list.append(sum(ai[i:i+M]))
    max_sum = max(sum_list) # 최대합
    min_sum = min(sum_list) # 최소합
    result.append((test_case, max_sum - min_sum)) 
for t, res in result:
    print(f&quot;#{t} {res}&quot;)
