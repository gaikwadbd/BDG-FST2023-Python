class Fruit(object):

    def __init__(self):
        print("I am a fruit")

    def nutrition(self):
        print("I am full of vitamins")

    def fruitShape(self):
        print("Every fruit can have different shape")

class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("I am Orange")

    def nutrition(self):
        print("I am full of vitamin c")

    def color(self):
        print("I keep it simple, the color is also orange")

f = Fruit()
f.nutrition()
f.fruitShape()

o = Orange()
o.nutrition()
o.fruitShape()
o.color()