n = open("SW Expert Academy\Programming Intermediate_list2\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):
    # 주어지는 정수 갯수
    N = int(n.readline())
    # 정수로 리스트를 받기 -> 문자열로 받아서 정렬하면 9보다 10이 뒤로 정렬됨
    num_list = list(map(int, n.readline().split()))
    
    # 일단 숫자로 받아서 정렬
    num_list = sorted(num_list)

    ans = []
    while(1):
        # 받은 리스트를 다 사용했거나
        if len(num_list) == 0:
            break
        # 정답 10개가 다 찼다면 break
        elif len(ans) == 10:
            break   
        
        # 가장 큰수 append
        ans.append(num_list.pop())
        # 가장 작은수 append
        ans.append(num_list[0])
        del num_list[0]

    # 각 요소 문자열로
    for i in range(len(ans)):
        ans[i] = str(ans[i])

    # 공백을 기준으로 연결
    ans = ' '.join(ans)
    
    print(f'#{test_case} {ans}')