n = open("SW Expert Academy\Programming Intermediate_String\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):

    # N : N x N 의 글자판
    # M : M길이의 회문 찾기
    N, M = map(int, n.readline().split())
    
    # 문자열을 글자 하나씩 리스트로 넣음
    box = []
    for _ in range(N):
        box.append(list(n.readline().rstrip()))
    
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
            if M%2 == 1:
                front_temp = []
                # 세로로 회문 앞부분을 탐색하여 리스트로 만들고 문자열로 저장
                for x in range(int(M/2)):
                    try:
                        front_temp.append(box[j+x][i])
                    except:
                        pass
                # 뒤집어서 저장
                front_part = ''.join(reversed(front_temp))

                # 세로로 회문 뒷부분을 탐색하여 리스트로 만들고 문자열로 저장
                back_temp = []
                for x in range(int(M/2)+1,2*int(M/2)+1):
                    try:
                        back_temp.append(box[j+x][i])
                    except:
                        pass
                back_part = "".join(back_temp)
                
                # 회문이라면 세로로 문자열 출력
                ans_temp = []
                if front_part == back_part:
                    for x in range(2*int(M/2)+1):
                        ans_temp.append(box[j+x][i])
                    ans = ''.join(ans_temp)
            else:
                # M(회문길이) 짝수일때
                front_temp = []
                for x in range(int(M/2)):
                    try:
                        front_temp.append(box[j+x][i])
                    except:
                        pass
                front_part = ''.join(reversed(front_temp))
                back_temp = []
                for x in range(int(M/2),2*int(M/2)):
                    try:
                        back_temp.append(box[j+x][i])
                    except:
                        pass
                back_part = "".join(back_temp)

                ans_temp = []
                if front_part == back_part:
                    for x in range(2*int(M/2)):
                        ans_temp.append(box[j+x][i])
                    ans = ''.join(ans_temp)

    print(f'#{test_case} {ans}')