#10단계: 재귀
#4. 하노이탑

def hanoi(n,a,b,c):

    if n == 1:           
        print(a,c)        # 1개 (n이 1일 때)까지 나눴으면 출력하기

    else:                    
        hanoi(n-1,a,c,b)      # 먼저 원반이 1개가 될때까지 아래 써둔 방식대로 나누기 // 1개까지 나누눈 것은 이 한 문장으로 됨
                              # 1개 (n == 1)이 되면 위에서 출력 함 (N이 짝수일 때 1번 원판은 1,2 으로  // N이 홀수일 때 1번 원판은 1,3로 시작됨)

        print(a,c)            # 1개 (n == 1)일 때의 위에 문장과 다르게 출력하기 위해
        hanoi(n-1,b,a,c)      # 1개 (n == 1)일 때의 위위 문장과 위에 문장과 다르게 출력하기 위해


n = int(input())
a = "1"
b = "2"
c = "3"

print((2**n)-1)
hanoi(n,a,b,c)


#Point
# 총 원판의 갯수 N개가 있을 때, 게속 n-1개씩 반복해서 옆으로 옮기는 작업
# ex) n=4일 때 , (4개 -> c로 이동하기 위해, 3개 -> b로 이동) , (3개 -> b로 이동하기 위해, 2개 -> c로 이동) ... 1개  
# 반대로 과정 출력

# 하노이탑 원판의 계산횟수 = (2의 n승 - 1)

# 의 경우 재귀함수 먼저 계산 후 print 나중에 계산 (거꾸로 계산한다고 생각, (hanoi+print 세트))
#hanoi(n-1)   ->   hanoi(2)     ->   hanoi(1)
#print(n)          print(3)          print(2)
#                                    print(3)