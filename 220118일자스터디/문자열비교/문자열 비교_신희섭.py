n = open("SW Expert Academy\Programming Intermediate_String\input.txt", "r")

T = int(n.readline())


for test_case in range(1, T + 1):
    # A: 찾을 문자열 / B: 전체 문자열
    A = n.readline().rstrip()
    B = n.readline().rstrip()

    ans = int(A in B)
    
    print(f'#{test_case} {ans}')