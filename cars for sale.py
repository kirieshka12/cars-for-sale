
class Car():
    def __init__(self, horse_power, color, label, weight):
        self.horse_power = horse_power
        self.color = color
        self.weight = weight
        self.label = label

    def sound(self):
        print('звучу')
    def drive(self):
        print('езжу')

passat_b5_universal = Car(horse_power = 130,color = 'Malinovi', label = 'volkswagen', weight=1350)
lada_granta = Car(horse_power=98, color = 'black', label = 'lada', weight=1200)
chevrolet_camaro = Car(horse_power=609, color= 'yellow', label = 'chevrolet', weight=1500)
