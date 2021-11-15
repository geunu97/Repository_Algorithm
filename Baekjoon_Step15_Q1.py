#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#1. 피보나치 함수

T = int(input())

def fibo(i):
    answer_list.append([answer_list[i-2][0] + answer_list[i-1][0], answer_list[i-2][1] + answer_list[i-1][1]])

for _ in range(T):
    answer_list=[[1,0],[0,1]]   

    a = int(input())

    if a != 0 or a != 1:
        for x in range(2,a+1):  
            fibo(x)

    print(answer_list[a][0],answer_list[a][1])


    #피보나치를 구현하라는 문제가 아니고
    #단지 피보나치 규칙에서 0과1이 몇번 들어갈지 알아보기 위한 문제
    #위에 처럼 푼게 메모이제이션!!!!!!!!!!!(바로 앞에 수를 바로 구하기 위해서 0부터 순서대로 값을 넣어둬서 저장함
    #                                      똑같은 값을 처음부터 또 계산할 필요가 없다)
