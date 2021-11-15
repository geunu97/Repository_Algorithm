#16단계: 그리디 알고리즘 (탐욕법)
#4. 잃어버린 괄호


start = input()

#-55+30    55+30
#-55-30    55 , 30
if start[0] == '-':                                  #맨 앞에 수가 -로 시작할 때
    list_a = list(start.split('-'))                  #-를 기준으로 모두 나누기 ( 55 , 50+40 )      
    total = 0
    for i in list_a:                                 
        sum = 0

        for j in i.split('+'):                       #-를 기준으로 나눈 수들을 인덱스 하나당 차례대로 +로 나눠주기 (인덱스 하나당 다 더한 후 -붙이기)
            sum += int(j)                            #규칙 : 55 - (50+40) - (x + y)...
        total -= sum

else:                                                #맨 앞에 수가 +로 시작할 때
    list_a = list(start.split('-'))                  #-를 기준으로 모두 나누기 ( 55 , 50+40 )
    total = 0
    start = 0
    for i in list_a:
        sum = 0

        if start == 0:                               #맨 앞에 수만 더해주고 시작하기 위해
            for j in i.split('+'):
                sum += int(j)
            total += sum
            start += 1
        
        else:                                        #위에 규칙과 동일
            for j in i.split('+'):
                sum += int(j)
            total -= sum
            
print(total)


#a.split('-')  , a.split('+')의 활용이 중요한 문제