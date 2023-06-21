# pass
# : 블록(영역)에서 아무런 동작을 수행하지 않을 때 사용하는 키워드

def func():
    # 구현할 내용이 없는 경우
    pass

func()

a = 10
if a > 10:
    # 아직 동작할 코드를 파악하지 못한 경우
    pass
else:
    print('test')
    
'''
    # match
    # : 변수, 표현식을 여러 패턴에 따라서 매칭해주는 조건문
    
    match 표현식:
        case 값1:
            실행문
        case 값2:
            실행문
        ...
        default:
            모두 매치가 되지 않는 경우

'''

menu = input('메뉴 번호 : ')
menu = int(menu)

match menu:
    case 1:     print('돈까스')
    case 2:     print('나시고랭')
    case 3:     print('삼겹살')
    case _:     print('기타')
    # case default:
    #     print('메뉴없음')