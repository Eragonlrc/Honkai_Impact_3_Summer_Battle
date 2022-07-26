import random

from hero import Hero


class VillV(Hero):
    """
    维尔薇
    生命: 100; 攻击: 20; 防御: 12; 速度: 25
    主动技能(创(造)力): 每3回合发动，对对手造成自己攻击力的伤害，并使对手陷入混乱状态(效果：对手下次普通攻击伤害返还自身，无视回合数)
    被动技能(大变活人): 回合开始时若维尔薇血量低于31，则自身与对手回复10~20点生命值(生命值回复分别计算)，并永久提升自身2~15点攻击力(每场比赛最多触发1次)
    """

    def __init__(self, h=100, a=20, d=12, sp=25):
        super().__init__(h, a, d, sp)
        self.name = "维尔薇"
        self.limited = False    # 被动使用标志

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 被动判定
        if self.health < 31 and not self.limited:  # 血量低于31，未使用过限定技
            print("维尔薇发动技能[大变活人]")
            self.heal(random.randint(10, 20))
            opnt.heal(random.randint(10, 20))
            attack_plus = random.randint(2, 15)
            self.attack += attack_plus
            print("维尔薇攻击力提升" + str(attack_plus) + "点，当前攻击力" + str(self.attack))
            self.limited = True
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 创(造)力
            phy = self.attack
            opnt.status['chaos'] = 1
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("维尔薇发动技能[创(造)力]")
            print("维尔薇对" + opnt.name, end="")
            opnt.suffer(self, physical=phy)
            print(opnt.name + "进入混乱状态，下次普通攻击时生效，伤害返还给自身")
        if opnt.health == 0:    # 对方战败
            return
        # 状态更新
        self.status_change(act)
