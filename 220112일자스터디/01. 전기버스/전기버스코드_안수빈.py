result=[]
T=int(input())
for test_case in range(1, T+1):
    K,N,M = map(int, input().split())
    charge_idx = list(map(int, input().split())) # 충전기 인덱스
    bus_line = [1 if i in charge_idx else 0 for i in range(N+1) ] # 버스 노선 : 충전기 위치 1로 표시    
    start = 0
    end = K
    cnt=0
    
    while True:
        zero = 0
        for i in range(start+1, end+1):
            if bus_line[i] == 1: # 충전기가 있는 위치를 시작으로 바꿔줌
                start = i
            else:
                zero += 1
        if zero == K: # K만큼 이동할 동안 충전기가 없다 -> 이동내에 종점 도달 불가
            cnt = 0
            break
        
        cnt +=1 # 위의 for문 및 if문 과정 끝나고 이동수는 1 증가
        end = start + K # 시작 위치에서 최대까지
        
        if end >= N: # 마지막인덱스가 종점보다 클경우 종료
            break
    result.append((test_case, cnt))
    
for t,count in result:
    print(f&quot;#{t} {count}&quot;)
