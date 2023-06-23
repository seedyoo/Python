'''
    # 상속 유형
    - 단일 상속
    - 다중 상속
    - 다단계 상속 
    - ...
    
    ## 단일 상속
    ```
        class A:
            pass
        class B(A):
            pass
    ```
    
    ## 다중 상속
    ```
        class A:
            pass
        class B(A):
            pass
        class C(A, B):          # 다중 상속
            pass
    ```
    
    ## 다단계 상속
    ```
        class A:
            pass
        class B(A):
            pass
        class C(B):             
            pass
    ```

'''
class BasicCar:
    def basicCarMethod(self):
        print('BasicCar - basicCarMethod() 메소드')
        
    def commonMethod(self):
        print('BasicCar - commonMethod() 메소드')
        
class SpeedCar:
    def speedCarMethod(self):
        print('SpeedCar - speedCarMethod() 메소드')
        
    def commonMethod(self):
        print('SpeedCar - commonMethod() 메소드')
        
# 다중 상속
class SuperCar(BasicCar, SpeedCar):
    
    def testMethod(self):
        # super() 부모 클래스에 대한 임시 객체 
        # * 다중 상속 시, 해당 메소드가 어느 부모 클래스의 메소드인지 모를 때 사용
        super().speedCarMethod()
        
        # * 다중 상속 시, 부모 클래스를 특정해서 메소드를 호출
        BasicCar.commonMethod(self)
        SpeedCar.commonMethod(self)



superCar = SuperCar()
superCar.basicCarMethod()
superCar.speedCarMethod()

# 2개 이상의 부모 클래스를 다중 상속하는 경우,
# 같은 이름의 메소드 호출 시, 나열된 클래스 중 첫 번째 클래스의 메소드가 실행된다
superCar.commonMethod()

superCar.testMethod()

