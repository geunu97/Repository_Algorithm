#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#6. 삼각형 (위에서부터 내려오는데 최대합 경로 구하기)

n = int(input())

list_t = []
for i in range(n):
    list_a = list(map(int,input().split()))
    list_t.append(list_a)


#가장 중요!!! 현재줄에서 최대일지라도 전체 합이 최대가 아닐 수 있다!!!!!!!!!!!!!!!!!   (여러 경우의 수 같이 구하고, 마지막에 최대의 합 비교해보면 됨!)
#dp (처음부터 순서대로 다음 값에 이전 값 더하기)
#바로 이전 문제와 거의 똑같음, 이전문제랑 같이 정리해서 써놓기!!!

for i in range(1,n):
    list_t[i][0] += list_t[i-1][0]
    list_t[i][-1] += list_t[i-1][-1]

    if i >= 2:
        for j in range(1,i):
            list_t[i][j] += max(list_t[i-1][j-1],list_t[i-1][j])



print(max(list_t[n-1]))





