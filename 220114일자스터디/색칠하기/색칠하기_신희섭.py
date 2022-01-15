import sys

n = open("SW Expert Academy\Programming Intermediate_list2\input.txt", "r")

T = int(n.readline())

# 색칠할 범위, 색상, 팔레트를 입력받아 색칠하는 함수
def coloring(r1, c1, r2, c2, color, box):
    for i in range(c1, c2 + 1):
        for j in range(r1, r2 + 1):
            box[i][j] += color

    return box

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(n.readline())  # 입력갯수

    # 기본 팔레트
    box = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # 입력갯수만큼 반복문
    for x in range(N):
        # 입력범위와 색깔을 입력받아 색칠 함수 실행
        r1, c1, r2, c2, color = map(int, n.readline().split())
        coloring(r1, c1, r2, c2, color, box)
    
    # 각 요소에서 1과 2가 둘다 칠해진 결과인 
    # 숫자 3을 카운팅한다. 
    ans = 0
    for li in box:
        ans += li.count(3)
     
    print(f'#{test_case} {ans}')