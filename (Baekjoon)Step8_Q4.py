#8단계: 기본 수학 1
#4. 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#   달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
#   또, 정상에 올라간 후에는 미끄러지지 않는다.
#   달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

import math

a,b,v = map(int,input().split())

answer = math.ceil((v - a) / (a - b)) + 1
print(answer)


#정상에 도착했으면 미끄러지지 않는다는 말이 중요!!
#반복문 사용X, 범위가 너무 큼
#전에 한번 풀었던 문제랑 비슷하게 풀었음

