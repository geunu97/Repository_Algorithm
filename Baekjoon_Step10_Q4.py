#10단계: 재귀
#4. 하노이탑

def hanoi(n,a,b,c):

    if n == 1:            #1번 원반 (N이 짝수일 때 1번 원판은 1,2 으로  // N이 홀수일 때 1번 원판은 1,3로 시작됨)
        print(a,c)        #마지막 원반 1개 이동하기

    else:                     #1.원반 n-1개가 2번으로 옮겨지는 과정까지 작업
        hanoi(n-1,a,c,b)      #1.먼저 원반이 1개가 될때까지 아래 써둔 방식대로 나누기 (b,c왔다갔다 반복해서 나누는 것)
        print(a,c)            # 위의 과정을 반대로 출력 함 + 가장 큰 원반 3번으로 옮기는 작업 출력
        hanoi(n-1,b,a,c)      # 위의 방법과 똑같이 b에 있는 n-1개 원반을 c로 옮기는 작업시작 (아래 써둔 방식대로 또 나누는 것)


n = int(input())
a = "1"
b = "2"
c = "3"

print((2**n)-1)
hanoi(n,a,b,c)


#Point
# 총 원판의 갯수 N개가 있을 때, 게속 n-1개씩(가장 밑에 있는 원반 제외) 반복해서 옆으로 옮기는 작업
# ex) n=4일 때 , (4개 -> c로 이동하기 위해, 3개 -> b로 이동) , (3개 -> b로 이동하기 위해, 2개 -> c로 이동) ... 1개  
# 반대로 과정 출력

# 하노이탑 원판의 계산횟수 = (2의 n승 - 1)

# 의 경우 재귀함수 먼저 계산 후 print 나중에 계산 (거꾸로 계산한다고 생각, (hanoi+print 세트))
#hanoi(n-1)   ->   hanoi(2)     ->   hanoi(1)
#print(n)          print(3)          print(2)
#                                    print(3)