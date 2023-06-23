# 포함 관계

class Motor:
    
    # 생성자
    def __init__(self):
        self.distance = 0
    
    # 앞으로 가기
    def forward(self):
        print('앞으로 이동')
        self.distance += 1
    
    # 뒤로 가기
    def backward(self):
        print('뒤로 이동')
        self.distance -= 1
    
class Robot:
    
    def __init__(self):
        # 포함 관계
        # 한 클래스가 다른 클래스의 멤버로 포함되는 관계
        self.motor = Motor()
        
    def __str__(self):
        return '이동 한 거리 : {}'.format( self.motor.distance )
    
import random
robot = Robot()

for i in range(10):
    if random.randint(0, 1):        # random.ranint(0, 1) : 0~1 사이의 랜덤 수
        robot.motor.forward()
    else:
        robot.motor.backward()
        
print(robot)
    
        
        