T = int(input()) # 테스트 케이스 수
result = []
for test_case in range(1,T+1):
    N=int(input()) # 카드 장 수
    ai = list(map(int, input())) #숫자 입력
    set_a = set(ai) # unique한 값들만 남김
    num_count={a:ai.count(a) for a in set_a} # 숫자와 개수 딕셔너리
    max_count = max(num_count.values()) # 개수 최대값 지정
    cnt=0 # 최댓값이 중복인지 확인하기 위해 횟수 카운트
    max_list=[] # 숫자와 개수 최댓값 리스트
    
    # 최댓값의 개수를 cnt에 그리고 그때의 숫자를 max_list에 저장
    for nc in num_count.items(): 
        if nc[1] == max_count:
            cnt+=1
            max_list.append(nc)
    # 최댓값이 한개면 그대로 출력
    if cnt==1:
        result.append((test_case, max_list[0]))
    # 최댓값이 여러개면 max인 숫자로 출력
    else:
        result.append((test_case, max(max_list)))

for i, res in result:
    print(f&quot;#{i} {res[0]} {res[1]}&quot;)
