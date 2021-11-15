#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#3. 01타일

    

# 1  2  3  5  8 ...
# 15746 으로 나눈 나머지를 구하라는 이유
# 직접 찾은 점화식 f(n) = f(n-1) + f(n-2)
'''
#     1 , 00 

N = 1  # 1                                                       1개

N = 2  # 11 , 00                                             2개

N = 3  # 111 , 100 , 001                                         3개


N = 4  # 0011 , 0000 , 1001, 1100 , 1111                     5개

N = 5  # 10000 , 00001 , 00100 , 11100 , 11111 , 00111  , 11001 , 10011       8개

'''


dictionary = {
    1:1,
    2:2
}

a = int(input())
#a = a % 15746        #이 말이 아님....

for i in range(3,a+1):
    dictionary[i] = (dictionary[i-1] + dictionary[i-2]) %15746      #이 말 이였음....

print(dictionary[a])




# 이렇게 하면 메모리 초과됨 !!!   print(dictionary[a] % 15746)
# 딕셔너리 사용해도 똑같음 !!!





#직접 점화식 구하는 문제...?
