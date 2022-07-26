import random
from hero import Hero


class Mobius(Hero):
    """
    梅比乌斯
    生命: 100; 攻击: 21; 防御: 11; 速度: 23
    主动技能(栖影水枪): 每3回合发动，对对手造成33点伤害并有33%的概率使对手陷入昏迷状态(无法行动)至对手下次行动阶段结束
    被动技能(不稳定物质): 普通攻击造成伤害时有33%的概率使对手陷入腐蚀状态，防御力永久下降3点，最多下降至0点(混乱状态下触发时状态返还自身)
    """

    def __init__(self, h=100, a=21, d=11, sp=23):
        super().__init__(h, a, d, sp)
        self.name = "梅比乌斯"

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 栖影水枪
            phy = 33
        # 伤害结算
        damage = 0
        if act == 1:
            damage = self.basic_attack(opnt, phy)
        elif act == 2:
            print("梅比乌斯发动技能[栖影水枪]")
            print("梅比乌斯对" + opnt.name, end="")
            opnt.suffer(self, physical=phy)
            if random.random() < 0.33:  # 33%概率
                opnt.status['stunned'] = 1
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['silenced'] == 0:    # 未被沉默
            if act == 1 and damage != 0:    # 普通攻击且造成伤害
                if random.random() < 0.33:  # 33%概率
                    print("梅比乌斯发动技能[不稳定物质]")
                    if damage > 0:  # 未被混乱
                        opnt.defence -= 3
                        print(opnt.name + "防御力下降3点，当前防御" + str(opnt.defence))
                    elif damage < 0:  # 被混乱
                        self.defence -= 3
                        print("梅比乌斯防御力下降3点，当前防御" + str(self.defence))
        # 状态更新
        self.status_change(act)
