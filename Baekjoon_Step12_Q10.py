#12단계: 정렬
#10. 좌표 압축

import sys
input = sys.stdin.readline

N = int(input())

list_a = list(map(int,input().split()))
list_list = list_a         #2 4 -10 4 -9

list_a = set(list_a)       #2 4 -10 -9

list_a = sorted(list_a)    #-10 -9 2 4

dictionary = { }
k = 0
for i in list_a:                      #리스트 X , 딕셔너리로  => 해당 키 값에 대한 value 불러오는 것 때문에 
    dictionary[i] = k  
    k += 1

for j in list_list:                   #반목문 리스트로 돌리기!!
    print(dictionary[j],end=" ")       

'''
list_b=[]
for i in range(len(list_a)):
    list_b.append([list_a[i],i])          #[-10,0] , [-9,1] , [2,2] , [4,3]
'''


