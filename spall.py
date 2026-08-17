from abc import Spell

class Fireball(Spell):
    '''Класс магии Огненный шар'''
    def __init__(self):
        self.name = 'Fireball'
        self.damage = 35
        self.mana_cost = 15
    
    def cast(self):
        return self.damage

class IceLance(Spell):
    '''Класс магии Ледяное сияние'''
    def __init__(self):
        self.name = 'IceLance'
        self.damage = 25
        self.mana_cost = 10
    
    def cast(self):
        return self.damage
    
class LightningBolt(Spell):
    '''Класс магии Удар молнии'''
    def __init__(self):
        self.name = 'LightningBolt'
        self.damage = 40
        self.mana_cost = 20
    
    def cast(self):
        return self.damage