# TODO: there's code missing in one or more lines below
class Base:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        return ""


class Circle(Base):

    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}


        , - ~ ~ ~ - ,
    , '               ' ,
  ,                       ,
 ,                         ,
,                           ,
,                           ,
,                           ,
 ,                         ,
  ,                       ,
    ,                  , '
      ' - , _ _ _ ,  '      
"""


class Square(Base):

    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
---------------------
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
---------------------
"""



# All of the code below is correct
def draw_any_shape(myShape):
    print(myShape.draw())

def main():
    s = Square(1,2,3)
    draw_any_shape(s)
    c = Circle(2,2,1)
    draw_any_shape(c)


main()
