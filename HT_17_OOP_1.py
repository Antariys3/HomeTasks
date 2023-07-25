
class Auto:
    def __init__(self, brand, age, mark, cоlor="white", weight=1600):
        self.brand = brand
        self.age = age
        self.cоlor = cоlor
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def bitthday(self):
        self.age += 1

    def stop(self):
        print("stop")
