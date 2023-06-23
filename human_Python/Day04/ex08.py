'''
    # 상속
    - 부모 클래스의 변수와 메소드를 자식 클래스에서 재사용하는 것
    
'''

# 부모 클래스 - Robot
class Robot:
    
    # 생성자
    def __init__(self, name, power, battery):
        self.name = name
        self.power = power
        self.battery = battery
        
    # 메소드 - 전원, 이동, 충전
    def power(self, power):
        self.power = power
        print('power : ', power)

    def move(self, direction):
        print('{} (으/로) 이동합니다'.format(direction))
        
    def charge(self):
        self.battery = 100
        print('충전이 완료되었습니다')
        
# ----class Robot 끝----
    
    

# 자식 클래스 _ DroneRobot, ClenaRobot
# 상속 정의 : class 클래스(부모클래스):

class DroneRobot(Robot):
    # 부모 클래스의 변수와 메소드를 모두 재사용한다
    # 단, 비공개 멤버(private)는 상속되지 않음
    # 최대 높이
    max_height = 50
    
    def __init__(self, name, power, battery, height):
        # super() : 자식 클래스의 생성자에서 부모클래스를 가져오는 메소드
        super().__init__(name, power, battery)
        self.height = height
        
    # 메소드 오버라이딩
    def move(self, direction, height):
        if height > DroneRobot.max_height:
            print('{}m 이상으로는 비행할 수 없습니다'.format(DroneRobot.max_height))
            return
        
        self.height = height
        print('{} 으(/로) 방향으로 비행합니다'.format(direction))
        print('고도 : {}'.format(height))
         
        
        
# ----class DroneRobot 끝---- 

'''
    자식클래스 정의 : CleanRobot   (로봇청소기)
    - 부모클래스 : Robot
    
    - 정의할 내용
        - 클래스 속성 : max_bin 속성을 선언 후 값 50으로 초기화
                      *max_bin : 먼지통의 최댓값
        - 생성자 
        - move() 메소드 오버라이딩
            * 출력 : {방향} 으(/로) 이동하여 청소합니다.
            * 기능 : 
            - 이동을 할 때마다 먼지 bin 을 1 씩 증가시킨다 (먼지 흡입)
            - 먼지통이 꽉차면, "더 이상 청소할 없습니다. 먼지통을 비워주세요..." 출력
                     
        
        - mapping() 메소드  * '청소할 영역을 기억합니다.'
        
        - vacate() 메소드   
            * 출력 : '먼지통을 비웁니다.'
            * 먼지통 비우는 기능
    
    - 실행할 내용
        1. CleanRobot 객체 생성
        2. mapping()
        3. move('앞쪽')
        3. move('왼쪽')
        3. move('뒤쪽')
        4. vacate()
'''

class CleanRobot(Robot):
    max_bin = 50
    
    def __init__(self,name, power, battery, bin=0):
        super().__init__(name, power, battery)
        self.bin = bin
        
    # 메소드 오버라이딩
    def move(self, direction):
        print('{} (으/로) 이동합니다'.format(direction))
        
        if( self.bin >= CleanRobot.max_bin ):
            print('더 이상 청소할 없습니다. 먼지통을 비워주세요...')
            return
        self.bin += 1           # 먼지 흡입
        
    def mapping(self):
        print('청소할 영역을 기억합니다.')
        
    def vacate(self):
        self.bin = 0
        print('먼지통을 비웁니다.')
        


# 객체 생성
print('# Robot #')
robot = Robot('휴먼로봇', 'ON', 100)
robot.move('왼쪽')
robot.charge()


print('# DroneRobot #')
drone = DroneRobot('드론로봇', 'ON', 100, 10)
drone.move('앞쪽', 50)


print('# CleanRobot #')
cleanRobot = CleanRobot('로봇청소기', 'ON', 100, 0)
cleanRobot.mapping()
cleanRobot.move('앞쪽')
cleanRobot.move('왼쪽')
cleanRobot.move('뒤쪽')
cleanRobot.vacate()



    
        
    

