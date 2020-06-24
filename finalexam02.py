import math
print('201911267 컴퓨터공학부 이성찬\n')


class location:

    x=0
    y=0
    
    def __init__(self,a,b):
        self.x=a
        self.y=b
    
    def distance(self,other):
        a=self.x-other.x
        b=self.y-other.y
        d=math.sqrt((a*a)+(b*b))
        print('점과 점 사이의 거리 : \n',format(d,'.4f'))
    
    def __add__(self,other):
        print('좌표 값의 합 : \nx : {} y: {}'.format(self.x+other.x,self.y+other.y))
        

p1=location(1,1)
p2=location(2,2)
p1.distance(p2)
p1+p2
