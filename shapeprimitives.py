import cv2 as cv    
class Shape:

    def __init__(self,onset, pos=(0, 0)):
        self.onset_time = onset
        self.area = 0
        self.perimeter = 0
        self.position = pos
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.age = 0

    def area(self):
        pass

    def perimeter(self):
        pass
    def update(self):
        self.age += 1
    def draw(self, canvas):
        pass
    def is_finished(self):
        return self.age > 100

class Circle(Shape):
    def __init__(self, onset,pos=(0, 0)):
        super().__init__(onset, pos)
        self.radius = 15.


    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def update(self):
        self.age += 1
        #map radius to age with mapping function
        self.radius = self.radius + 3

    def draw(self, canvas):
        cv.circle(canvas, self.position, int(self.radius), (255,255,255),1 )
    