#9단계: 기본 수학 2
#4. M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

m,n = map(int,input().split())

for i in range(m,n+1):
    finish = 0

    if i == 1:
        continue

    else:
        sqrt_num = int(i ** 0.5)

        for j in range(2,sqrt_num+1):
            if i % j == 0:
                finish = 1
                break

        if finish != 1:
            print(i)


        # !! 2부터 정수 제곱근+1 까지 반복문 돌리면 됨
        # 주어진 수 % i (루트, 정수, 2 ~ n-1까지 반복문 돌린 수) == 0 이면 아님