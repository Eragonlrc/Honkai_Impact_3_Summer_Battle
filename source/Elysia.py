import random
from hero import Hero


class Elysia(Hero):
    """
    爱莉希雅
    生命: 100; 攻击: 21; 防御: 8; 速度: 20
    主动技能(夏梦之花): 每2回合发动，对对手造成25~50点伤害并使对手下次行动时攻击力下降6点(行动不包括释放被动技能)
    被动技能(水花溅射): 攻击后有35%概率追加一次溅射攻击，造成11点元素伤害(混乱状态下触发时伤害返还给自身)
    """

    def __init__(self, h=100, a=21, d=8, sp=20):
        super().__init__(h, a, d, sp)
        self.name = "爱莉希雅"

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 2)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 夏梦之花
            phy = random.randint(25, 50)
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("爱莉希雅发动技能[夏梦之花]")
            print("爱莉希雅对" + opnt.name, end="")
            opnt.suffer(self, phy)
            print(opnt.name + "下次行动时攻击力下降6点")
            opnt.status['weak'] = 1
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['skip'] + self.status['silenced'] == 0:  # 不被跳过、沉默
            if random.random() < 0.35:  # 35%概率
                print("爱莉希雅发动技能[水花溅射]")
                print("爱莉希雅对" + opnt.name + "追加一次溅射攻击，", end="")
                if self.status['chaos'] == 1:   # 混乱状态下伤害返还
                    print("混乱状态生效，爱莉希雅对爱莉希雅", end="")
                    self.suffer(self, elemental=11)
                else:
                    opnt.suffer(self, elemental=11)
        # 状态更新
        self.status_change(act)