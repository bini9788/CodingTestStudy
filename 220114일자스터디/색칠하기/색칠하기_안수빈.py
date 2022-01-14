T = int(input()) # 테스트 케이스 수
result = []
for test_case in range(1, T + 1):
    grid = [[0]*10 for _ in range(10)]
    N = int(input()) # 칠할 영역의 개수
    
    # 영역 개수 만큼 인덱스 입력받고 색칠하기 반복
    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                grid[r][c] += color
    
    # 다 색칠 후 숫자가 3인 것을 count
    purple_count=sum([row.count(3) for row in grid])
    result.append((test_case, purple_count))
[print(f&quot;#{t} {cnt}&quot;) for t, cnt in result]
