n = open("SW Expert Academy\Programming Intermediate_String\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):

    # N : N x N 의 글자판
    # M : M길이의 회문 찾기
    N, M = map(int, n.readline().split())
    
    # 문자열을 글자 하나씩 리스트로 넣음
    # 가로로 추가
    box = []
    # 세로로 추가
    box_2 = [[]*N for _ in range(N)]
    for _ in range(N):
        temp = list(n.readline().rstrip())
        box.append(temp)
        for i, t in enumerate(temp):
            box_2[i].append(t)
            
    # 가로 탐색
    for i in range(N):
        for j in range(N):
            # M(회문길이) 홀수일때
            if M % 2 == 1:
                front_part = ''.join(reversed(box[i][j:j+int(M/2)])) # 회문 탐색 앞부분(미리 뒤집는다)
                back_part = ''.join(box[i][j+1+int(M/2):j+1+2*int(M/2)]) # 회문 탐색 뒷부분
                if front_part == back_part: # 회문이라면
                    ans = ''.join(box[i][j:j+M]) # 처음인덱스~마지막인덱스 문자열 출력
            # M(회문길이) 짝수일때
            else:
                front_part = ''.join(reversed(box[i][j:j+int(M/2)]))
                back_part = ''.join(box[i][j+int(M/2):j+2*int(M/2)])
                if front_part == back_part:
                    ans = ''.join(box[i][j:j+M])

    # 세로탐색
    for i in range(N):
        for j in range(N):
            # M(회문길이) 홀수일때
            if M % 2 == 1:
                front_part = ''.join(reversed(box_2[i][j:j+int(M/2)])) # 회문 탐색 앞부분(미리 뒤집는다)
                back_part = ''.join(box_2[i][j+1+int(M/2):j+1+2*int(M/2)]) # 회문 탐색 뒷부분
                if front_part == back_part: # 회문이라면
                    ans = ''.join(box_2[i][j:j+M]) # 처음인덱스~마지막인덱스 문자열 출력
            # M(회문길이) 짝수일때
            else:
                front_part = ''.join(reversed(box_2[i][j:j+int(M/2)]))
                back_part = ''.join(box_2[i][j+int(M/2):j+2*int(M/2)])
                if front_part == back_part:
                    ans = ''.join(box_2[i][j:j+M])

    print(f'#{test_case} {ans}')