n = open("SW Expert Academy\Programming Intermediate_list2\input.txt", "r")

T = int(n.readline())

# 이진 탐색 함수
# 시작 페이지, 전체 페이지, 찾아야할 페이지, 탐색횟수
def book_search(l , r, target, cnt = 0):
    # 중간페이지 설정
    c= int((l+r)/2)

    # 찾아야할 페이지와 중간 페이지를 비교하여 진행
    if target == c:
        cnt += 1
        return cnt
    elif target > c:
        cnt += 1
        return book_search(c, r, target, cnt)
    else:
        cnt += 1
        return book_search(l, c, target, cnt)

for test_case in range(1, T + 1):
    # P: 전체 페이지수 / A: A가 찾을 쪽수 / B: B가 찾을 쪽수
    P, A, B = map(int, n.readline().split())
    
    # 각 경우 탐색횟수 계산
    cnt_A = book_search(1, P, A)
    cnt_B = book_search(1, P, B)

    # 비교하여 결과 출력
    if cnt_A == cnt_B:
        ans = 0
    elif cnt_A > cnt_B:
        ans = 'B'
    else:
        ans = 'A'

    print(f'#{test_case} {ans}')