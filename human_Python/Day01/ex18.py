# 논리 연산자
# and       : A and B
#           - A 와 B 모두 True(참) 일때, 결과가 (True)이다.
# 쇼트서킷
# A and B   : A가 False 이면, B 를 검사하지 않는다.

# or        : A or B
#           - A 와 B 둘 중 하나의 조건이라도 True(참)이면, 결과가 True(참)이다
# not
# A or B   : A가 True 이면, B 를 검사하지 않는다.

# not       : True 이면 False, False 이면 True 로 변경한다.
a = 10
b = 5

print('{} > 7 and {} > 7 : {}'.format(a, b, a > 7 and b > 7))
print('{} > 7 or {} > 7 : {}'.format(a, b, a > 7 or b > 7))

print('not : {} : {}'.format(a, not a))     # 0 이 아닌 값에 not 연산 → False
print('not : {} : {}'.format(a, not 0))     # 0 또는 False 에 not 연산 → True