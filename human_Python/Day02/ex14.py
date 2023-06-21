'''
    사용자 함수
    : 사용자가 직접 정의한 함수
    
    # 함수 전의 키워드 : def
    
    def 함수명( 매개변수1, 매개변수2, ... ):
        실행할 문장
        실행할 문장
        return (값)

    # return
    1. 함수를 종료
    2. (값)을 함수를 호출한 자리로 반환
'''

a = 10
b = 2
def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

print('a + b = {}'.format( plus(a, b) ))
print('a - b = {}'.format( minus(a, b) ))
print('a * b = {}'.format( mul(a, b) ))
print('a / b = {}'.format( div(a, b) ))