#10단계: 재귀
#4. 하노이탑

def hanoi(n,a,b,c):

    if n == 1:
        print(a,c)

    else:
        hanoi(n-1,a,c,b)  
        print(a,c)
        hanoi(n-1,b,a,c)


n = int(input())
a = "1"
b = "2"
c = "3"

print((n**2)-1)
hanoi(n,a,b,c)

