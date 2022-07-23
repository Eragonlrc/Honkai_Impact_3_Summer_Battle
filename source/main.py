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
c = 0
for i in range(1000000):
    e = Elysia()
    g = Griseo()
    b = Battle(e, g)
    b.run()
    if b.winner.name == '爱莉希雅':
        c += 1
print('爱莉希雅胜率：' + str(c/1000000))
