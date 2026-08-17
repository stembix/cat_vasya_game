from character import Character
from monster import Monster
from Spell import Fireball, IceLance, LightningBolt


def main():
    print("=== Демонстрация работы RPG системы ===\n")

    print("1. Создание персонажа-воина:")
    warrior = Character(
        'warrior',
        strength=15,
        dexterity=10,
        constitution=14,
        wisdom=8,
        intelligence=10,
        charisma=12
    )
    print(f"Класс: {warrior.character_class}")
    print(f"Здоровье: {warrior.current_health}/{warrior.max_health}")
    print(f"Урон: {warrior.damage}")
    print(f"Защита: {warrior.defense}")
    print(f"Мана: {warrior.mana}")
    print()

    print("2. Создание персонажа-мага:")
    mage = Character(
        'mage',
        strength=8,
        dexterity=12,
        constitution=10,
        wisdom=16,
        intelligence=18,
        charisma=14
    )
    print(f"Класс: {mage.character_class}")
    print(f"Здоровье: {mage.current_health}/{mage.max_health}")
    print(f"Урон: {mage.damage}")
    print(f"Защита: {mage.defense}")
    print(f"Мана: {mage.mana}")
    print()

    print("3. Создание монстра:")
    monster = Monster(
        strength=12,
        dexterity=8,
        constitution=15,
        wisdom=5,
        intelligence=6,
        charisma=4
    )
    print(f"Здоровье монстра: {monster.current_health}/{monster.max_health}")
    print(f"Урон монстра: {monster.damage}")
    print(f"Защита монстра: {monster.defense}")
    print()

    print("4. Демонстрация работы с заклинаниями:")

    fireball = Fireball()
    icelance = IceLance()
    lightning = LightningBolt()

    mage.add_spell(fireball)
    mage.add_spell(icelance)
    mage.add_spell(lightning)

    print(f"Изученные заклинания мага: {[spell.name for spell in mage.spells]}")
    print(f"Текущая мана: {mage.mana}")

    try:
        damage = mage.cast_spell(0)
        print(f"Применено заклинание {mage.spells[0].name}, урон: {damage}")
        print(f"Осталось маны: {mage.mana}")
    except RuntimeError as e:
        print(f"Ошибка: {e}")

    print("\n5. Попытка использовать заклинание без маны:")
    try:
        warrior.add_spell(fireball)
        warrior.cast_spell(0)
    except RuntimeError as e:
        print(f"Ошибка: {e}")

    print("\n6. Проверка валидации класса персонажа:")
    try:
        invalid = Character('invalid_class', 10, 10, 10, 10, 10, 10)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")


if __name__ == "__main__":
    main()