T = int(input())
result = []
for test_case in range(1,T+1):
    N = int(input()) #정수의 개수
    ai = list(map(int, input().split())) #정수 리스트
    sorted_ai = sorted(ai) # 정렬하기
    num_list = []
    for i in range(5): # 5개의 최대최소값의 쌍을 출력
        max_num = sorted_ai.pop() # 현재 리스트에 남아있는 값의 최댓값
        min_num = sorted_ai.pop(0) # 현재 리스트에 남아있는 값의 최소값
        num_list.extend([max_num,min_num])
    result.append((test_case, num_list))   
for t, res in result: #결과 출력
    print(f"#{t}", end=" ")
    for r in res:
        print(r, end=" ")
    print()
