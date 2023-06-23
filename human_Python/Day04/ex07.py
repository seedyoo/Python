
class Circle:
    
    @property
    def radius(self):
        return self.__radius
    
    
    @radius.setter
    def radius(self, value):
        print('setter 메소드 호출...')
        if value <= 0:
            print('반지름은 양수이어야합니다.')
            self.__radius = 0
            return
        
        self.__radius = value
        
    @radius.getter
    def radius(self):
        print('getter 메소드 호출...')
        return self.__radius

circle = Circle()

circle.radius = -10
print('circle - radius : {}'.format( circle.radius ))
        