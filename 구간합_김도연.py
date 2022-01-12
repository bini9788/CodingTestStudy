T = int(input())
sumMax=0
sumMin=0
result=0
total_list=[]
# N:숫자 개수, M:구간 선택
for test_case in range(1, T + 1):
    N, M=map(int, input().split())
    num=list(map(int, input().split()))
    
    # 아래 다 되짚어보기
    for i in range(N-M+1):
        total=0
        for m in range(M):
            total+=num[m+i]
        total_list.append(total)
    sumMax=max(total_list)
    sumMin=min(total_list)
    result=sumMax-sumMin
    print(f'#{T} {result}')