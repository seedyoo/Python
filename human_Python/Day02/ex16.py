'''
    다중 반환
    : 파이썬에서는 하나의 반환값도 처리할 수 있고,
      여러 개의 반환값도 처리할 수 있다
      
    def 함수명 (매개변수):
        실행문
        실행문
        return (값1),(값2),(값3), ...
        
'''

def calculate( *args ):
    result1 = sum(args)
    result2 = max(args)
    result3 = min(args)
    result4 = sum(args) / len(args)
    # t = (result1, result2, result3, result4)
    # return t
    return result1, result2, result3, result4
    # 반환값을 튜플로 생성하여 반환한다
    
a, b, c, d = calculate(1,2,3,4,5)
result = calculate(1,2,3,4,5)

print('a : {}'.format(a))
print('b : {}'.format(b))
print('c : {}'.format(c))
print('d : {}'.format(d))

print('result : {}'.format(result))


