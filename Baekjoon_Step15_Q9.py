#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#9. 쉬운 계단 수


N = int(input())

list_a = [1] * 10
list_a[0] = 0
for _ in range(1,N):
    new =[0] * 10
    for i in range(10):
        if i == 0:
            new[1] += list_a[i]
        elif i == 9:
            new[8] += list_a[i] 
        else:
            new[i-1] += list_a[i]
            new[i+1] += list_a[i]
    list_a = new

print(int(sum(list_a) % 1000000000))


'''
10    #0과 9로 끝날 때만 변수,
12

21
23

..

87
89

98
'''



''' 
#점화식 찾는 거는 fake
f(n) = f(n-1) * 2  - (n-1)

f(1) = 9
f(2) = 17
f(3) = 32
f(4) = 61
'''

