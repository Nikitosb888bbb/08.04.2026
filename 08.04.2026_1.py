class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg


monster = Monster()
m1 = Monster("Дракула",120, 35)
m2 = Monster("Люкан", 100, 40)

print(f'Имя: {monster.name}, Здровье: {monster.hp}, Урон: {monster.dmg}')
print(f'Имя: {m1.name}, Здоровье: {m1.hp}, Урон: {m1.dmg}')
print(f'Имя: {m2.name}, Здоровье: {m2.hp}, Урон: {m2.dmg}')
