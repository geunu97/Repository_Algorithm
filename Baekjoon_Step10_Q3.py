#10단계: 재귀
#3번 문제

def star(num):
    if num == 3:
        list_b[0][:3] = 1
        list_b[1][0] = 1
        list_b[1][2] = 1
        list_b[1][1] = 0
        list_b[2][:3] = 1 



num = int(input())

list_a=[]
list_b=[]

for i in range(num):
    list_a.append(0)

for j in range(num):
    list_b.append(list_a)

star(num)



#2차원 리스트 사용

#프랙탈 : 작은 구조가 전체 구조와 닮은 형태로 끝없이 되풀이되는 구조




'''
n = 9일 때

*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
'''




