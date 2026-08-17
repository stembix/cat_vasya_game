from abc import ABC, abstractmethod


class Unit(ABC):
    '''Абстрактный класс для всех Юнитов'''

    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength  # сила
        self.dexterity = dexterity  # ловкость
        self.constitution = constitution  # телосложение
        self.wisdom = wisdom  # мудрость
        self.intelligence = intelligence  # интеллект
        self.charisma = charisma  # харизма
        self.spells = []  # Список изученных заклинаний
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    def add_spell(self, spell):
        self.spells.append(spell)

    def cast_spell(self, index):
        spell = self.spells[index]

        if self.mana < spell.mana_cost:
            raise RuntimeError(
                f"Недостаточно маны! Нужно {spell.mana_cost}, имеется {self.mana}"
            )

        self.mana -= spell.mana_cost
        return spell.cast()


class Spell(ABC):
    '''Абстрактный класс для всех заклинаний'''

    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        pass