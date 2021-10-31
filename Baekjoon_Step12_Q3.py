#12단계: 정렬
#3. 수 정렬하기3   (카운팅정렬)

import sys
input = sys.stdin.readline

a = int(input())

list_a = [0] * 10001     #주어진 범위 1~10000   , #해당 범위 인덱스까지 모두 값0 넣어놓기  #표현 알아놓기(리스트인데 안에서 곱셈하기)
#                                                                                       #반복문 + append로 해도 됨
for i in range(a):
    list_a[int(input())] += 1           #받은 숫자들 해당 인덱스에 카운팅 시작

for i in range(10001):
    if list_a[i] != 0:
        for j in range(list_a[i]):      #1부터 10001까지 돌면서 카운팅 된거 하나씩 출력하기
            print(i)                    #해당 인덱스 값으로 출력

