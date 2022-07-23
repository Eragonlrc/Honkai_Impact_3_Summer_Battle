from battle import Battle
from Aponia import Aponia
from Eden import Eden
from Elysia import Elysia
from Griseo import Griseo
from Hua import Hua
from Kalpas import Kalpas
from Kevin import Kevin
from Kosma import Kosma
from Mobius import Mobius
from Pardofelis import Pardofelis
from Sakura import Sakura
from VillV import VillV
ca, cs = 0, 0
for i in range(100000):
    s = Sakura()
    a = Aponia()
    b = Battle(s, a)
    b.run()
    if b.winner.name == '阿波尼亚':
        ca += 1
    else:
        cs += 1
print('阿波尼亚胜率：' + str(ca/100000))
