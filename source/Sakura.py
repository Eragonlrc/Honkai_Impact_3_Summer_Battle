import random

from hero import Hero


class Sakura(Hero):
    """
    樱
    生命: 100; 攻击: 24; 防御: 10; 速度: 27
    主动技能(夏之型·瓜切): 每2回合发动，回复自身1~5点生命值(最多回复至100点)，并对对手造成1.3倍自身攻击力的伤害(倍数伤害不计算小数点之后的数值)
    被动技能(夏之型·樱流): 受到攻击时有15%的概率闪避本回合所有攻击(不受沉默影响，无法闪避状态伤害)
    """

    def __init__(self, h=100, a=24, d=10, sp=27):
        super().__init__(h, a, d, sp)
        self.name = "樱"

    def suffer(self, opnt, physical=0, elemental=0):
        """
        樱的被动通过重构suffer函数实现
        """
        if self.status['skip'] == 0:    # 自身未被封印或昏迷
            if random.random() < 0.15:  # 15%概率
                self.status['miss'] = 1
        if self.status['miss'] == 1:    # 本回合的所有攻击都会被闪避
            print('未造成伤害，樱闪避本次攻击')
        else:
            super(Sakura, self).suffer(opnt, physical=physical, elemental=elemental)

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 2)
        # 伤害计算
        phy, val = 0, 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 夏之型·瓜切
            val = random.randint(1, 5)
            phy = int(self.attack * 1.3)
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("樱发动技能[夏之型·瓜切]")
            self.heal(val)
            print("樱对" + opnt.name, end="")
            opnt.suffer(self, physical=phy)
        if opnt.health == 0:    # 对方战败
            return
        # 状态更新
        self.status_change(act)
