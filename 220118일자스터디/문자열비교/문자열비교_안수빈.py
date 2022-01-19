T = int(input())
for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    if str2.find(str1) != -1: # find : 찾으려는 문자가 있으면 인덱스 반환, 없으면 -1 반환
        print(f"#{test_case} 1")
    else :
        print(f"#{test_case} 0")
