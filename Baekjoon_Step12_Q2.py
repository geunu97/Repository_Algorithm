#12단계: 정렬
#2. 수 정렬하기2

import sys

a = int(input())

list_a=[]
for i in range(a):
    list_a.append(int(sys.stdin.readline()))  #int() 형변환으로 공백 없앨 수 있음(rstrip() 대신 사용가능)
                                              #특히 반복문에서 사용

list_a.sort()        # sort 퀵소트 지원
 
for j in range(a):
    sys.stdout.write(str(list_a[j]) + "\n")    #str만 가능
 