'''
    # property (프로퍼티)
    - 객체의 속성에 제한된 접근을 하도록 지정한 속성
    
    # property 정의
    - @property 데코레이터를 getter, setter 메소드에 정의
    
    * getter 메소드 → @property 
    * setter 메소드 → @속성명.setter
    
    
    # property 정의2
    
    @property
    def 변수명(self):
        return self.__변수명
    
    @변수명.getter
    def 변수명(self):
        return self.__변수명
    
    @변수명.setter
    def 변수명(self, value):
        self.__변수명 = value
    
'''

class Person:
    
    # __속성 : 클래스 외부에서 접근 제한
    @property
    def name(self):
        return self.__name
    
    @name.getter        # getter
    def name(self):
        return self.__name
    
    @name.setter        # setter
    def name(self, value):
        self.__name = value
# Person 끝


p = Person()

p.name = '김휴먼'        
print(' p - name : {}'.format( p.name ) )
        
        
        
p2 = Person()

p2.name = '박휴먼'        
print(' p2 - name : {}'.format( p2.name ) )
        

    
    
        
