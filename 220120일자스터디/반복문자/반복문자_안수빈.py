T = int(input())

for test_case in range(1,T+1): 
    str_ = input()
    stack = []                         # 문자를 저장할 스택 지정
    for i in range(len(str_)):         # 문자열 길이만큼 반복문 실행
        if len(stack) ==0 :            # 스택에 원소가 없을때는 우선 추가
            stack.append(str_[i]) 
        else:                     
            if stack[-1] == str_[i]:   # 스택의 마지막 원소와 현재 원소가 동일한 문자라면
                stack.pop()            # 스택의 마지막 원소를 제거
            else:
                stack.append(str_[i])   # 동일하지 않은 문자라면 스택에 원소 추가
    print(f"#{test_case} {len(stack)}") # 남은 원소의 길이를 출력
