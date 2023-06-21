# continue
# - 뒤의 남은 실행문을 건너뛰고, 다음 반복으로 넘어가는 키워드


# 짝수의 합계
a = 0
sum = 0
while a <= 20:
    a = a + 1
    # 홀수인 경우를 넘어가도록
    if a % 2 == 1:
        continue
    sum += a

print('1~20 사이의 짝수의 합계 : {}'.format(sum))