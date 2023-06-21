'''
    내장 함수
    : 외부에 따로 정의한 모듈에 있는 함수가 아니라
      파이썬 미리 정의가 되어 있는 함수
      "바로 사용할 수 있는 함수"
'''

# 문자열 내장 함수
'''
    1. chr()
    : 특정 문자의 유니코드 값을 입력하면,
      해당 문자를 반환하는 함수
      
    2. ord()
    : 특정 문자를 입력하면,
      해당 문자의 유니코드를 반환하는 함수
      
    3. eval()
    : 표현식을 문자열로 입력하면 표현식의 연산결과를 반환하는 함수
    ex) eval('100+200') --> 300
        a = 10
        eval('a * 5 )   --> 50
        
    4. format()
    : 전달받은 값과 포맷코드에 따른 형식 문자열을 반환하는 함수
    
    5. str()
    : 전달받은 인수를 문자열로 반환하는 함수
    ex) str(10) ---> '10'
'''
# chr
print( chr(97) )        # a
print( chr(98) )        # b
print( chr(65) )        # A
print( chr(66) )        # B

# ord
print( ord('a') )       # 97
print( ord('b') )       # 98
print( ord('A') )       # 65
print( ord('B') )       # 66

# eval
expr = input('수식을 입력 : ')
result = eval(expr)
print('계산 결과 : ' + str(result))

# format
print( format(100000000, ',') )

# str
print( str(1.5) )