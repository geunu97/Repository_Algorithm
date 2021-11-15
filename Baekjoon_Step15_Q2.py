#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#2. 신나는 함수 실행

dictionary = { }

def dp(a,b,c):
    key = "{} {} {}".format(a,b,c)     #값이 3개여도 편하게 키값 형식 설정해놓기

    if a <= 0 or b <= 0 or c <= 0:     #이거는 따로 배놔야 됨!!!!! (특정 값이 아니기 때문)
        return 1


    if key in dictionary:
        return dictionary[key]
    
    else:
        if a > 20 or b > 20 or c > 20:
            dictionary[key] = dp(20, 20, 20)
            return dictionary[key]

        if a < b and b < c:
            dictionary[key] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
            return dictionary[key]

        else:
            dictionary[key] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
            return dictionary[key]


#dictionary[1,2,3] 이런건 없음 

while True:
    a,b,c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d) = %d"%(a,b,c,dp(a,b,c)))


#동적계획법(메모이제이션) 문제!
#딕셔너리 사용!



