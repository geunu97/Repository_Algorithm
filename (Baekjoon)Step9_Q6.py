#9단계: 기본 수학 2
#6번 문제

a = int(input())

for i in range(a):
    b = int(input())

    for j in range(b//2,b+1):   # 주어진 수/2 부터 하나의 값만 먼저 구하기 
        finish = 0

        sqrt_num = int(j**0.5)
        for k in range(2,sqrt_num+1):
            if j % k == 0:
                finish = 1
                break
        if finish != 1:
            number_2 = j
            number_1 = b - j
            ffinish = 0

            sqrt_num = int(number_1**0.5)
            for k in range(2,sqrt_num+1):
                if number_1 % k == 0:
                    ffinish = 1
                    break

            if ffinish != 1:
                print(number_1,number_2)
                break