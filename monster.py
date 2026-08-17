from base import Unit


class Monster(Unit):
    '''Класс Монстров'''

    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.mana = 0

    def calculate_max_health(self):
        return self.constitution * 8 + self.strength // 3

    def calculate_damage(self):
        return self.strength * 2 + self.constitution // 5

    def calculate_defense(self):
        return self.constitution * 1.2 + self.strength // 5