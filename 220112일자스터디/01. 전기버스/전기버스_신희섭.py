# 전기버스

import sys
n = open("sample_input.txt", "r")

T = int(n.readline())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # K: 최대이동거리, N: 종점 정류장, M: 충전기 있는 정류장 갯수
    K, N, M = map(int, n.readline().split())
    num_list = list(map(int, n.readline().split()))

    current = N
    cnt = 0

    while(1):
        if current - K <= 0:
            break

        temp = []
        flag = current - K
        for i in num_list:
            if i >= flag:
                temp.append(i) 

        if len(temp) != 0:
            current = min(temp)
            cnt += 1
            del num_list[-len(temp):]
        else:
            cnt = 0
            break
            
    print(f'#{test_case} {cnt}')