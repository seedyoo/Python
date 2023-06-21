'''
    - 지역변수
    : 함수 내부에서 선언한 변수
      함수 내부에서만 접근 가능하고, 외부에서는 접근 불가
    
    
    - 전역변수
    : 함수 외부에서 선언한 변수
      함수 내부, 외부 모든 영역에서 접근 가능

'''

def func():
    a = 10      # 지역변수
    print('func() 내부 - a : {}'.format(a))
    
    
func()          # 함수호출


# print('func() 내부 - a : {}'.format(a))
# 에러 발생
# NameError: name 'a' is not defined

b = 10          # 전역변수

def test():
    print('test() 내부 - b : {}'.format(b))
    
    
test()          # 함수호출
print('test() 외부 - b : {}'.format(b))
