# 모듈
'''
    모듈
    : 변수나 함수 또는 클래스를 모아놓은 파이썬 파일
    - 하나의 파이썬 파일(.py)
    
    모듈 사용
    import 모듈명
'''

# converter 모듈
# : 규격이나 단위를 변환하는 함수를 제공하는 모듈
# 모듈 설치
# pip install converter  
# pip uninstall converter
import converter
from converter import *


# 150km --> miles 로 변환
miles = kilometer_to_miles(150)
print('150km = {} miles'.format(miles))

# 1000g --> pound 로 변환
pound = gram_to_pound(1000)
print('1000g = {} pound'.format(pound))