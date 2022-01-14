
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())
    b = input().rstrip()
    
    count_dict = {}
	
    # 숫자마다 돌면서 있으면 +1, 없으면 추가 -> 숫자 : 빈도 리스트 생성
    for i in b:
        if i in count_dict.keys():
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    # 최대값을 받아옴
    max_value = max(list(count_dict.values()))
    temp = []

    # 
    for i in list(count_dict.keys()):
        if count_dict[i] == max_value :
            temp.append(i)

    if list(count_dict.values()).count(max_value) > 2:
        max_key = max(temp)
        print(f'#{test_case} ' + max_key, count_dict[max_key])
    else:
        max_key = max(count_dict, key=count_dict.get)
        print(f'#{test_case} ' + max_key, count_dict[max_key])