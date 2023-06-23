# getter, setter
# - getter : 값을 가져오는 메소드 -> get_변수명()
# - setter : 값을 지정하는 메소드 -> set_변수명()  

class Person:
    
    # getter
    def get_name(self):
        return self.name
    
    # setter
    def set_name(self, value):
        self.name = value
        
        
p = Person()

p.set_name('김휴먼')
print('p - name : {}'.format( p.get_name() ))
        
    