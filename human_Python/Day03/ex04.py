'''
    표준 모듈
    1. math         : 수학 연산관련 모듈
    2. random       : 랜덤 수 생성 모듈
    3. time         : 시간 처리 모듈
    4. datetime     : 날짜/시간 처리 모듈
'''
import math

# 원주율
print('math.pi : {} '.format( math.pi ))

# 올림
print('math.ceil(1.1) : {} '.format( math.ceil(1.1) ))

# 내림
print('math.floor(1.9) : {} '.format( math.floor(1.9) ))

# round() 반올림 - 기본 내장 함수 (버전 3.9이상)
print('round(2.5, 1) : {} '.format( round(2.5, 1) ))
print('round(2.4, 1) : {} '.format( round(2.4, 1) ))

# 파이썬 버전 3.9 부터는 --> 내장 함수 (math.round() 제거)
# 파이썬 버전 3.9 이하  --> math.round()
# print('math.round(2.5,1) : {} '.format( math.round(2.5,1)))
# print('math.round(2.4,1) : {} '.format( math.round(2.4,1)))

# 파이썬에서의 round() 함수 특징
# x.5
# 원래 값과 올림한 값의 차이 = 원래 값과 내림한 값의 차이가 같은 경우 (0.5)
# 짝수가 되는 크기로 올림 또는 내림한다

print( round(0.5) )         # 1
print( round(1.5) )         # 2
print( round(2.5) )         # 3
print( round(3.5) )         # 4
print( round(4.5) )         # 5
print( round(5.5) )         # 6

print('------------------')

print( round(1.12567, 1) )
print( round(1.12567, 2) )
print( round(1.12567, 3) )

# 절사
# - 소수점 아래를 버림하고 정수 부분만을 반환
print('math.trunc(1.9) : {} '.format( math.trunc(1.9)))
# print('math.trunc(1.125,2) : {} '.format( math.trunc(1.125,2)))

# 제곱근
print('math.sqrt(9) : {} '.format( math.sqrt(9)))

# 제곱
print('math.pow(3,2) : {} '.format( math.pow(3, 2)))