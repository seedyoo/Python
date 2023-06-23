'''
    주소록 프로그램 만들기
    # 메뉴
    1. 주소 등록하기
    2. 주소 삭제하기
    3. 주소 수정하기
    4. 주소 검색하기
    5. 주소록 전체 출력하기
    0. 프로그램 종료

'''

import sys
'''
    sys 모듈
    : 인터프리터가 제공하는 변수와 함수를 통해서
      프로세스를 직접 제어할 수 있게 해주는 모듈
      sys.exit()        : 프로그램 종료
'''

# 사람
class Person:
    # 변수 : name, phone, addr
    # 메소드 : info()
    
    # 생성자
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr
        
    # info
    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))
        
        

# 주소록
class AddressBook:
    # 변수 : 주소 리스트 - address_list
    
    # 생성자
    def __init__(self):
        self.address_list = []
        self.file_reader()      # 저장된 주소록 불러오기
        
    
    # 파일 생성
    def file_generator(self):
        
        try:
            file = open('AddressBook.csv', 'wt', encoding='UTF-8')
        except:
            print('AddressBook.csv 파일을 생성할 수 없습니다.')
        else:
            # address_list 를 반복하여, 모든 연락처 정보를 .csv 파일에 출력
            for person in self.address_list:
                file.write('{},{},{}\n'.format(person.name, person.phone, person.addr))
            
            print('AddressBook.csv 파일이 저장되었습니다')
            
            file.close()
        
    # 파일 읽기
    def file_reader(self):
        
        # 예외 처리 
        try:
            # 예외 발생가능성이 있는 코드
            file = open('AddressBook.csv', 'rt', encoding='UTF-8')
        except:
            # 예외 발생 시, 예외 처리 코드
            print('AddressBook.csv 파일이 없습니다')
            self.file_generator()
            self.file_reader()
        else:
            # 예외 미발생 시, 실행할 코드
            while True:
                buffer = file.readline()
                if not buffer:
                    break
                
                # 김휴먼,010-1234-1234,서울시 영등포구
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                # rstrip(문자) : 지정한 문자를 문자열의 오른쪽에서 제거
                # 서울시 영등포구\n  --> '\n' 제거 
                addr = buffer.split(',')[2].rstrip('\n')
                
                # print('이름 : {}'.format(name))
                # print('전화번호 : {}'.format(phone))
                # print('주소 : {}'.format(addr))
                
                person = Person(name, phone, addr)
                
                # csv 파일의 연락처 목록을 address_list 리스트로 가져옴
                self.address_list.append(person)
            
            print('AddresssBook.csv 파일을 읽어왔습니다.')
            file.close()
        
            
        
        
    # 메뉴
    def menu():
        print('-' * 30)
        print('1. 주소 등록하기')
        print('2. 주소 삭제하기')
        print('3. 주소 수정하기')
        print('4. 주소 검색하기')
        print('5. 주소록 전체 출력하기')
        print('0. 프로그램 종료')
        print('-' * 30)
        choice = int( input('메뉴 번호 : ') )
        return choice
    
    # 프로그램 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()   
        
        
    # 프로그램 실행
    def run(self):
        # 메뉴를 호출
        while True:
            choice = AddressBook.menu()         # 입력한 메뉴번호
            if choice == 0: self.exit()         # 종료
            elif choice == 1: self.insert()     # 추가
            elif choice == 2: self.delete()     # 삭제
            elif choice == 3: self.update()     # 수정
            elif choice == 4: self.search()     # 검색
            elif choice == 5: self.print_all()  # 전체출력
            else: print('(0~5) 사이의 메뉴번호를 입력해주세요...')
            
            
    # 연락처 추가
    def insert(self):
        print('----- 새 연락처 추가 -----')
        name = input('등록할 이름 : ')
        phone = input('등록할 전화번호 : ')
        addr = input('등록할 주소 : ')
        
        # 유효성 검사
        
        # Person 객체 생성 및 name, phone, addr 속성 초기화
        person = Person(name, phone, addr)
        
        # AddressBook 클래스의 address_list 리스트에 생성된 객체 추가
        self.address_list.append(person)
        
        # 파일 저장 ( file_generator() )
        self.file_generator()
        
        print('새 연락처가 정상적으로 등록되었습니다.')
        
        
    # 연락처 삭제
    def delete(self):
        print('---- 기존 연락처 삭제 ----')
        name = input('삭제할 이름 : ')
        
        # list ['김휴먼1','김휴먼2']
        # enumerate(list) --> (0, '김휴먼1'), (1, '김휴먼2')
        for i, person in enumerate( self.address_list ):
            # 입력한 이름이 연락처 목록 존재?
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('검색한 전화번호가 "{}" 입니다'.format(phone))
                
                check = input('삭제할까요? (Y/N) : ').upper()
                if check == 'Y':
                    # "Y" 입력 시, 연락처 삭제
                    self.address_list.pop(i)
                    # 파일 저장
                    self.file_generator()
                    break
                elif check == 'N':
                    print('삭제를 취소하였습니다.')
                    
    
    # 주소록 수정
    def update(self):
        print('---- 기존 연락처 수정 ----')                
        name = input('수정할 이름 : ')
        if not name:
            print('이름을 입력하지 않아 수정을 취소합니다.')
            return
        
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('검색한 전화번호가 "{}" 입니다'.format(phone))
                
                check = input('수정할까요? (Y/N) : ').upper()
                
                if check == 'N':
                    continue
                
                if check == 'Y':
                    new_name = input('변경할 이름 : ')
                    new_phone = input('변경할 전화번호 : ')
                    new_addr = input('변경할 주소 : ')
                    
                    person = Person(new_name, new_phone, new_addr)
                    self.address_list[i] = person
                    
                    print('주소록이 수정되었습니다.')
                    print('수정된 정보')
                    
                    if i > 0: self.address_list[i-1].info()
                    self.address_list[i].info()
                    if i+1 < len(self.address_list): self.address_list[i+1].info()
                    
                    self.file_generator()
                    break
                
    # 연락처 검색
    def search(self):
        # 검색할 이름 입력
        name = input('검색할 이름 : ')
        
        
        print('---- 조회된 연락처 정보 ----')
        for i, person in enumerate(self.address_list):
            
            if name == self.address_list[i].name:
                person.info()
                
                
                
                
    # 주소록 전체 출력
    def print_all(self):
        print('---- 전체 연락처 출력 ----')
        for person in self.address_list:
            person.info()
            
        list_count = len(self.address_list)
        print('총 {}개의 연락처가 있습니다.'.format(list_count))

            
        
        
# 객체 생성       
app = AddressBook()

# 프로그램 실행
app.run()
