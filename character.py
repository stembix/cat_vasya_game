from base import Unit


class Character(Unit):
    '''Класс игрового персонажа'''

    val_class = ['warrior', 'mage', 'hunter']

    def __init__(self, character_class, strength, dexterity, constitution, wisdom, intelligence, charisma):
        if character_class not in self.val_class:
            raise ValueError(
                f"Некорректный класс персонажа: '{character_class}'. "
                f"Доступные классы: {', '.join(self.val_class)}"
            )

        self.character_class = character_class
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.mana = self.calculate_max_mana()

    def calculate_max_health(self):
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self):
        if self.character_class == 'warrior':
            return self.strength * 2.2 + self.constitution // 3
        elif self.character_class == 'mage':
            return self.intelligence * 2.5 + self.wisdom // 2
        elif self.character_class == 'hunter':
            return self.dexterity * 1.9 + self.strength // 3

    def calculate_defense(self):
        if self.character_class == 'warrior':
            return self.constitution * 1.8 + self.strength // 4
        elif self.character_class == 'mage':
            return self.wisdom * 1.3 + self.intelligence // 6
        elif self.character_class == 'hunter':
            return self.dexterity * 1.6 + self.constitution // 5

    def calculate_max_mana(self):
        if self.character_class == 'warrior':
            return self.intelligence + self.strength // 2
        elif self.character_class == 'mage':
            return self.intelligence * 3 + self.wisdom
        elif self.character_class == 'hunter':
            return self.dexterity * 1.5 + self.wisdom // 2