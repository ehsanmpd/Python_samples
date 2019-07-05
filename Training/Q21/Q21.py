class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def move(self,direction,step):
        if direction=="UP":
            self.y += step
        elif direction == "DOWN":
            self.y -= step
        elif direction == "LEFT":
            self.x -= step
        elif direction == "RIGHT":
            self.x += step

    def distance(self,nextPoint):
        return sqrt(pow(self.x-nextPoint.x,2)+pow(self.y - nextPoint.y,2))

    def current_position(self):
        return [self.x,self.y]

from math import sqrt

p = Point(0,0)
while True:
    line = input("Type direction step (to terminate type 0):")
    if line != '0':
        dirStep = line.split(' ')
        if len(dirStep)==2:
            p.move(dirStep[0],int(dirStep[1]))
        print("Current position: ",p.current_position())
    else:
        break

print("Distance: ",round(p.distance(Point(0,0))))