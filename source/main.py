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

# # 单场胜率模拟
# c = 0
# t = 10000
# for i in range(t):
#     e = Elysia()
#     a = Aponia()
#     b = Battle(e, a)
#     b.run()
#     if b.winner.name == '爱莉希雅':
#         c += 1
# print('爱莉希雅胜率：' + str(c/t))

# 枚举对手，功能性测试
l = [Aponia, Eden, Elysia, Griseo, Hua, Kalpas, Kevin, Kosma, Mobius, Pardofelis, Sakura, VillV]
for i in range(12):
    for j in range(i+1, 12):
        p1 = l[i]()
        p2 = l[j]()
        b = Battle(p1, p2)
        print(p1.name + ": 攻击: " + str(p1.attack) + "; 防御: " + str(p1.defence) + "; 速度: " + str(p1.speed))
        print(p2.name + ": 攻击: " + str(p2.attack) + "; 防御: " + str(p2.defence) + "; 速度: " + str(p2.speed))
        b.run()
        print('-' * 50)
