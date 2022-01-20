# 출처: https://totoma3.tistory.com/126


T=int(input()) 
def paper(N): 
    if N%10==0: 
        if N==10: #N=10일때 1반환 
            return 1 
        elif N==20: #20x20은 3반환 
            return 3 
        else: 
            return paper(N-10)+(2*paper(N-20)) 
        
for t in range(1, T+1): 
    N=int(input()) 
    cnt=paper(N) 
    print("#{} {}".format(t,cnt))

