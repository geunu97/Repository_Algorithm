#1단계: 입출력과 사칙연산
#11. (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다. 
#    (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

#입력조건 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
#출력조건 : 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

#예제입력 : 472
#           385

#예제출력 : 2360
#           3776
#           1416
#           181720

a = int(input())
b = int(input())

b_1 = b % 10
b_10 = int(b % 100 / 10)
b_100 = int(b / 100)

print(a*b_1)
print(a*b_10)
print(a*b_100)
print((a*b_1)+((a*b_10)*10)+((a*b_100)*100))