from base import Spell


class Fireball(Spell):
    '''Класс магии Огненный шар'''

    def __init__(self):
        super().__init__('Fireball', 35, 15)

    def cast(self):
        return self.damage


class IceLance(Spell):
    '''Класс магии Ледяное копье'''

    def __init__(self):
        super().__init__('IceLance', 25, 10)

    def cast(self):
        return self.damage


class LightningBolt(Spell):
    '''Класс магии Удар молнии'''

    def __init__(self):
        super().__init__('LightningBolt', 40, 20)

    def cast(self):
        return self.damage