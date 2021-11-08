#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#10. 포도주 시식

n = int(input())

dp=[0] #이건 편하게 계산하기 위해
for i in range(n):
    dp.append(int(input()))

if n <= 2:
    print(sum(dp))
else:
    list_sum = [0] * (n+1)
    list_sum[1] = dp[1]
    list_sum[2] = dp[1] + dp[2]
    #핵심
    for i in range(3,n+1):
        list_sum[i] = max(dp[i] + dp[i-1] + list_sum[i-3], dp[i] + list_sum[i-2], list_sum[i-1])
    print(list_sum[n])
