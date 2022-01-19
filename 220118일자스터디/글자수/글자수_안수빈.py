T = int(input())
for test_case in range(1, T+1):
    str1 = input()   		# 찾으려는 문자열
    str2 = input()     	    # str1을 포함하는 문자열
    max_count = 0     	# 문자 최대 개수를 지정
    for str_ in str1:       # str1 내 문자 하나씩 비교
        str_count = str2.count(str_)      # 문자 하나의 개수 세기
        if str_count > max_count:      # 기존의 max_count보다 크면 
            max_count = str_count       # max_count값을 바꿔줌
    print(f"#{test_case} {max_count}")    
