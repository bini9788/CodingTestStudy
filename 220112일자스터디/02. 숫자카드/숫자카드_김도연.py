T=int(input())

count_list=[]
for test_case in range(1, T+1):
    # 카드장수
    N=int(input())
    # 카드 숫자, 여백없이 주어짐
    a_list=list(map(str, input()))
    
    count_list=[0]*10
    for i in range(N):
        # 되짚어보기
        count_list[int(a_list[i])]+=1
    
    
    max_count=0
    max_card=0
    for i in range(len(count_list)):
        if i==(len(count_list)-1):
            break           
        elif max_count<=count_list[i+1]:
            max_count=count_list[i+1]
            max_card=i+1
        elif max_count>count_list[i+1]:
            max_count=max_count
            max_card=max_card
