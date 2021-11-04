#14단계: 백트래킹
#6. 스도쿠

list_a=[]
list_sudoku=[]
for i in range(9):
    list_a = list(map(int,input().split()))
    list_sudoku.append(list_a)


#가로 검사
for i in range(9):
    list_1_9 = [1,2,3,4,5,6,7,8,9]

    if list_sudoku[i].count(0) == 1:
        number_list = list(set(list_1_9) - set(list_sudoku[i]))
        number = number_list[0]

        for j in range(9):
            if list_sudoku[i][j] == 0:
                list_sudoku[i][j] = number
                break
for x in range(9):
    print(list_sudoku[x])

#세로 검사









'''
list_a = [1,2,3]
list_b = [1,2]
number_list = list(set(list_a) - set(list_b))  # 표현 알아놓기!!!!!   ,딕셔너리로 변환 -> 리스트 변환
number = number_list[0]
print(number)
'''


