#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#4. 파도반 수열

#파도반 수열 검색

T = int(input())

dictionary = {
    1:1,
    2:1,
    3:1
 }

def padoban(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = padoban(n-2) + padoban(n-3)
        return dictionary[n]

for i in range(T):
    n = int(input())

    print(padoban(n))

#피보나치 수열과 매우 비슷 
#재귀함수 + 딕셔너리 사용
#파도반 수열 첫번째, 두번째, 세번째 값 1 , f(x) = f(x-2) + f(x-1)
#더 자세한건 검색해서 노트에 써놓기
