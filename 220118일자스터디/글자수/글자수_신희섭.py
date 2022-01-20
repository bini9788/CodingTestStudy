n = open("SW Expert Academy\Programming Intermediate_String\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):
    # A: 셋을 만들 문자열 / B: 찾을 문자열
    A = n.readline().rstrip()
    B = n.readline().rstrip()

    # A의 문자열 하나씩 B에서 카운팅
    cnt = []
    for i in A:
        cnt.append(B.count(i))
    
    # 그중에 최대값이 정답
    ans = max(cnt)

    print(f'#{test_case} {ans}')
