#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#5. RGB 최소비용거리

n = int(input())

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1,n):                                    #핵심은 모두의 경우의 수(a,b,c일때로 다 계산) 최소 선택 후 합계로 한줄씩 내려오는 것!!!!!!!!!!!!!!!
    p[i][0] += min(p[i-1][1], p[i-1][2])                #예를 들어 2번째줄에서 a 선택했으면 위에 min(b,c) + 현재위치 a   한줄씩 반복계서 내려오면 됨   
    p[i][1] += min(p[i-1][0], p[i-1][2])                #예를 들어 2번째줄에서 b 선택했으면 위에 min(a,c) + 현재위치 b   한줄씩 반복계서 내려오면 됨 
    p[i][2] += min(p[i-1][0], p[i-1][1])                #예를 들어 2번째줄에서 c 선택했으면 위에 min(a,b) + 현재위치 c   한줄씩 반복계서 내려오면 됨 

print(min(p[n-1][0], p[n-1][1], p[n-1][2]))             #단순하게 마지막 줄에서의 최소값만 구해주면 됨


# a b c
# a b c
# a b c
# a b c
# a b c
#  ...

#이런식으로 N줄 있을 때 한 줄당 한개씩 선택해서 마지막까지 총 합계가 최소비용이 되야하는 문제
#단 조건은 특정 한줄에서 a를 선택했다면 바로 전줄 과 다음 줄은 a를 선택하 수 없다.

#dp인 이유는 나눠서 계산해야되며, 바로 전값을 알아야 다음값을 알 수 있기 때문  
# (해결 : 앞에서 부터 차례대로 계산해서 다음값을 저장했다)