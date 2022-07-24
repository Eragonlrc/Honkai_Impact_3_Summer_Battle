import random
from hero import Hero


class Kalpas(Hero):
    """
    千劫
    生命: 100; 攻击: 23; 防御: 9; 速度: 26
    主动技能(盛夏燔祭): 每3回合发动，燃烧自己10点生命值，对对手造成45点伤害并附加1~20点元素伤害，此后休息一回合(血量不足11点时无法发动)
    被动技能(夏之狂热): 生命值越低攻击力越高，每损失5点生命值提高1点攻击力(每次行动时触发)(不受沉默效果影响)
    """

    def __init__(self, h=100, a=23, d=9, sp=26):
        super().__init__(h, a, d, sp)
        self.name = "千劫"
        self.attack_plus = 0    # 额外攻击力

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 被动判定
        if act != 0:
            print("千劫发动技能[夏之狂热]")
            attack_plus_total = self.health // 5
            print("千劫攻击力永久提升" + str(attack_plus_total - self.attack_plus), end="，")
            self.attack += attack_plus_total - self.attack_plus
            self.attack_plus = attack_plus_total
            print("当前攻击力" + self.attack)
        # 伤害计算
        phy, ele = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 盛夏燔祭
            phy = 45
            ele = random.randint(1, 20)
            self.status['skip'] = 1
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("千劫发动技能[盛夏燔祭]")
            self.bleed(10)
            print("千劫对" + opnt.name, end="")
            opnt.suffer(self, physical=phy)
            print("千劫对" + opnt.name, end="")
            opnt.suffer(self, elemental=ele)
            self.status['rest'] = 1
            print("千劫下回合休息")
        # 状态更新
        self.status_change(act)
