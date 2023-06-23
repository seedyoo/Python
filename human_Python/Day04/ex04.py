# 인스턴스 변수, 메소드
# 클래스 변수, 메소드

'''
    class 클래스명:
        # 클래스 변수
        클래스변수명 = 값
        
        # 클래스 메소드
        @classmethod            # @???  : 데코레이터
        def 메소드명(cls):
            메소드 내용
            
        # cls : 클래스 자신을 가리키는 참조변수

'''

class Student:
    # 클래스 변수       - 객체간에 공유할 값으로 사용하는 변수
    count = 0
    student_list = []
    
    # 생성자
    def __init__(self, name, age, tel):
        # 인스턴스 변수 - 객체 별로 다르게 사용할 변수
        self.name = name
        self.age = age
        self.tel = tel
        Student.count += 1
        Student.student_list.append(self)
        
    # 클래스 메소드
    @classmethod
    def show_info(cls):
        for student in cls.student_list:
            print( str(student) )
            
    def __str__(self):
        return '{} / {} / {}'.format(self.name, self.age, self.tel)
# Student 끝            

s1 = Student('김휴먼', 20, '010-1111-2222')
s2 = Student('이효리', 30, '010-1111-2222')
s3 = Student('손석구', 40, '010-1111-2222')


# 클래스 속성 접근 : (클래스명).(속성)
print('{} 명의 학생이 참여하였습니다.'.format( Student.count ) )

# 클래스 메소드 호출 : (클래스명).(메소드)
print( Student.show_info() )

            
        