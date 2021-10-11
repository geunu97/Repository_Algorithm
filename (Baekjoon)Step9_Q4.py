#9단계: 기본 수학 2
#4. M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

m,n = map(int,input().split())

def sosu(i):
    sqrt_num = int(i**0.5)

    for j in range(3,sqrt_num+1,2):     #약수는 대칭성이 있어서 절반만 확인하면 소수인지 확인가능
        if i % j == 0:
            return False
    return True

for i in range(m,n+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
        continue
    elif i % 2 == 0:
        continue
    else:
        if sosu(i):
            print(i)

        # 2부터 int(제곱근+1) 까지 반복문 돌리면 됨 , 그 반복문 돌린 수가 주어진 수와 계산하면 됨
        # 주어진 수 % i == 0 이면 아님
        # 2 ~ 제곱근 까지만 계산하는게 포인트!!
        # 에라토스테네스의 체 (2의 배수 지우고, 3의 배수 지우고, 5의 배수 지우고, 첫 수는 소수 , ...)