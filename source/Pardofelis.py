import random

from hero import Hero


class Pardofelis(Hero):
    """
    帕朵菲莉丝
    生命: 100; 攻击: 17; 防御: 10; 速度: 24
    主动技能(沙滩寻宝): 每3回合发动，对对手造成30点伤害并使自身回复实际造成伤害的生命值(生命值最多回复至100点)
    被动技能(最佳搭档): 每次攻击有30%概率召唤罐头，对对手造成30点伤害(罐头攻击不受混乱状态影响)
    """

    def __init__(self, h=100, a=17, d=10, sp=24):
        super().__init__(h, a, d, sp)
        self.name = "帕朵菲莉丝"

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 沙滩寻宝
            phy = 30
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("帕朵菲利斯发动技能[沙滩寻宝]")
            print("帕朵菲利斯对" + opnt.name, end="")
            val = opnt.suffer(self, physical=phy)
            self.heal(val)
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['sealed'] + self.status['stunned'] + self.status['silenced'] == 0:  # 不被封印、昏迷、沉默
            if random.random() < 0.3:   # 30%概率
                print("帕朵菲利斯发动技能[最佳搭档]，本次攻击额外", end="")
                opnt.suffer(self, 30)
        # 状态更新
        self.status_change(act)
