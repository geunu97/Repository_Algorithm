#10단계: 재귀
#2. 피보나치 수 5

def fibo(a):
    if a == 0:
        return 0

    elif a == 1 or a == 2:
        return 1

    else:
        return fibo(a-1) + fibo(a-2)

a = int(input())

print(fibo(a))