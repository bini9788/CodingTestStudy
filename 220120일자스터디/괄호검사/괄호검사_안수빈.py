T = int(input())
for test_case in range(1,T+1):
    str_ = input()
    stack=[]                                     # 괄호를 저장할 스택 지정
    
    for i in range(len(str_)): 
        if (str_[i]=="(")|(str_[i]=="{"):       # 괄호의 시작은 무조건 스택에 추가
            stack.append(str_[i])     
        elif (str_[i]==")"):                    # 닫는 소괄호인 경우
           
            # stack[-1] 이 stack에 요소가 없는 경우 예외발생 -> 무조건 스택에 추가
            try:
                if (stack[-1]) == "(":          #스택의 마지막 원소가 시작 소괄호이면 시작 소괄호 제거
                    stack.pop()
                else:
                    stack.append(str_[i])
            except : 
                stack.append(str_[i])
        elif(str_[i]=="}"):
            try:
                if (stack[-1]) == "{":
                    stack.pop()
                else:
                    stack.append(str_[i])
            except : 
                stack.append(str_[i])
    
    # 스택에 남아있는 괄호를 확인
    if len(stack) ==0 :
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
    
