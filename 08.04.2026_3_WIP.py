class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(self.name)
        print(self.hp)
        print(self.dmg)


m1 = input ('Введите Имя, Здоровье и Урон монстра: ').split()
m2 = input ('Введите Имя, Здоровье и Урон монстра: ').split()

dracula = Monster(m1[0], m1[1], m1[2])
lycan = Monster(m2[0], m2[1], m2[2])

while True:
    m1.hp -= m2.dmg
    m2.hp -= m1.dmg
    if m2.hp <= 0:
        m2.hp = 0
    
    m1.ph -= m2.dmg
    m2.hp -= m1.dmg
