from itertools import combinations

n = open("SW Expert Academy\Programming Intermediate_list2\input.txt", "r")

T = int(n.readline())

# 부분집합 생성
num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
List = []
for i in range(1, len(num_list)+1):
    temp = combinations(num_list, i)
    List.extend(temp)

for test_case in range(1, T + 1):
    cnt = 0
    # N: 원소의 수 / M: 부분집합의 합
    N, M = map(int, n.readline().split())

    # 각 부분집합에 대해 조건을 탐색
    for i in List:
        if (len(i) == N) & (sum(i) == M):
            cnt += 1
    
    print(f'#{test_case} {cnt}')
