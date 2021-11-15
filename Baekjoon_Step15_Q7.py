#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#7. 계단 오르기

stairs = [0 for i in range(301)]

N = int(input())
sums = [0 for i in range(301)]

for i in range(N):
    stairs[i] = int(input())

sums[0] = stairs[0]
sums[1] = stairs[0] + stairs[1]

if N >= 2:
    sums[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

    for j in range(3, N):
        sums[j] = max(sums[j-3]+stairs[j-1]+stairs[j], 
                      sums[j-2]+stairs[j])

print(sums[N-1])

#마지막을 밟아야 하는 문제는 거꾸로 생각해야 됨

'''
- 마지막 계단은 무조건 밟아야 하므로, 이를 기준으로 생각해보자. 마지막 계단을 밟았을 때, 다음과 같이 두 경우로 나눌 수 있다.

   1) 마지막 계단의 전 계단을 밟음.
   2) 마지막 계단의 전전 계단을 밟음.

- 1)의 경우, 연속된 계단 3개를 밟을 수 없으므로, 마지막 계단의 전전계단은 밟을 수 없다. 그러므로 마지막 계단의 전전전 계단을 밟은 것이다.
- 이를 식으로 나타낼 경우 다음과 같다.
   1) sum[n] = sum[n-3] + stair[n-1] + stair[n]
   2) sum[n] = sum[n-2] + stair[n]
- 위 두 값 중 큰 값을 선택하여 최댓값을 구할 수 있다.
'''