T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    sum_list = []
    for i in range(N-M+1): 
        sum_list.append(sum(num_list[i:i+M]))
    
    ans = max(sum_list) - min(sum_list)
    print(f'#{test_case} {ans}')

    
 

