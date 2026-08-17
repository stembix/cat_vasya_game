from abc import Unit

class Monster(Unit):
    '''Класс Монстров'''
    def calculate_max_health(self):
        health = self.constitution * 8 + self.strength // 3

    def calculate_damage(self):
        damage = self.strength * 2 + self.self.constitution // 5

    def calculate_defense(self):
        defense = self.constitution * 1.2 + self.strength // 5