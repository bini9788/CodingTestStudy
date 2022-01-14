T = int(input())
A = list(range(1,12+1))
result=[]
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    cnt = 0 # 부분집합을 카운트할 변수 지정
    n=len(A) 
    for i in range(1<<n): #1<<n 비트 연산으로 0~2**n까지 부분집합의 개수 지정
        subset_sum=0
        subset=[]
        for j in range(n):
            if i&(1<<j): #i와 비트 연산으로 비교하면 인덱스(j)의 부분집합을 출력
                subset.append(A[j])
                subset_sum += A[j]
        if (len(subset )==N)&(subset_sum == K): # 길이가 N이고, 원소의 총합이 K인 경우 카운트
            cnt += 1
    result.append((test_case,cnt))
[print(f"#{t} {res}") for t, res in result]
