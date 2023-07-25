from HT_17_OOP_1 import Auto
import time


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, cоlor="black", weight=6800):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, cоlor="white", weight=1600):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)


volvo_FH_500 = Truck("Volvo", 8, "FH 500", 15000)
daf_FX = Truck("Daf", 9, "FX", 15000)

audi_A8 = Car("AUDI", 15, "A8", 280)
renault_clio = Car("Renault", 12, "Clio", 210)

print(volvo_FH_500.brand, volvo_FH_500.mark)
volvo_FH_500.load()
volvo_FH_500.move()
volvo_FH_500.bitthday()
volvo_FH_500.stop()
print()

print(daf_FX.brand, daf_FX.mark)
daf_FX.load()
daf_FX.move()
daf_FX.bitthday()
daf_FX.stop()
print()

print(audi_A8.brand, audi_A8.mark)
audi_A8.move()
audi_A8.bitthday()
audi_A8.stop()
print()

print(renault_clio.brand, renault_clio.mark)
renault_clio.move()
renault_clio.bitthday()
renault_clio.stop()
