'''
    클래스 선언
    
    class 클래스명:
        클래스 내용 (생성자, 소멸자, 메소드)
        
        # 생성자
        # : 객체가 생성될 때, 실행되는 메소드
        def__init__(self, 매개변수):
            생성자 내용
        
        # self : 객체 자신을 가리키는 키워드(딕셔너리)
        # self.(변수), self.(메소드)
        
        # 소멸자
        # : 객체가 소멸될 때, 실행되는 메소드
        def__del__(self):
            소멸자 내용
        
        # 메소드
        # : 클래스 내에서 정의된 함수
        def 메소드명(self, 매개변수):
            메소드 내용
'''

# Person 클래스 선언
class Person:
    
    # 생성자
    # def __init__(self):
    #     print('Person 객체 생성...')

    def __init__(self, name=None, age=None, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성...')
    
    
    # 소멸자
    def __del__(self):
        print('Person 객체 소멸...')
        
        
    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'
              .format(self.name, self.age, self.tel) )
# class Person 끝

# Person 객체 생성
person = Person()

# 객체의 변수 접근
person.name = '김휴먼'
person.age = 20
person.tel = '010-1234-1234'

print('이름 : ',person.name)
print('나이 : ',person.age)
print('전화번호 : ',person.tel)


person2 = Person('이휴먼', 20, '010-1111-2222')
print('이름 : ',person2.name)
print('나이 : ',person2.age)
print('전화번호 : ',person2.tel)


person3 = Person('박휴먼', 30, '010-0000-0000')
person3.show_info()


p = Person(name='aaa')
p.show_info()