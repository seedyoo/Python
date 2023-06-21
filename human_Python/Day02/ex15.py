'''
    # 가변 매개변수
    : 매개변수의 개수를 변경이 가능하도록 지정하는 매개변수
    
    - 매개변수 앞에 '*' 를 붙여서 가변 매개변수로 선언
    def 함수명( *매개변수 )
    
    # 디폴트 매개변수 (기본 매개변수)
    : 인수가 없는 경우, 기본값을 지정하는 매개변수
    def 함수명( 매개변수 = '기본값' )
    
'''

# *가변매개변수 : 전달인자를 튜플의 형태로 전달 받음
def add( *args ):
    print('{} 의 합계는 {} 입니다'.format( args, sum(args) ))
    
add(1,2)
add(1,2,3)
add(1,2,3,4)

# **가변매개변수 : 전달인자를 딕셔너리의 형태로 전달 받음
def teamList( team, **member ):
    print('팀 이름 : {}'.format(team))
    for m in member:
        print('{} ({})'.format(m, member.get(m) ))
        

teamList('A조', name='김휴먼', age=20)        
teamList('A조', name1='김휴먼', age1=20, name2='박휴먼', age2=30)        


def greet( name, msg='안녕하세요'):
    print('{} 님, {}'.format(name, msg))
    
greet('김휴먼')
greet('김휴먼', '반갑습니다')



