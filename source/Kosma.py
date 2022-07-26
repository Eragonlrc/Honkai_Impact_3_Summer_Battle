import random
from hero import Hero


class Kosma(Hero):
    """
    科斯魔
    生命: 100; 攻击:19; 防御: 11; 速度: 19
    主动技能(邪渊之钩): 每2回合发动，对对手造成4次攻击，每次攻击造成11~22点伤害，若对手处于撕裂状态，则每次攻击会额外附加3点元素伤害
    被动技能(不归之爪): 每次攻击结束有15%概率使对手陷入撕裂状态，从下回合开始每回合减少4点生命值，持续3回合，重复触发刷新状态(混乱状态下触发时状态返还自身)
    """

    def __init__(self, h=100, a=19, d=11, sp=19):
        super().__init__(h, a, d, sp)
        self.name = "科斯魔"

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 2)
        # 伤害计算
        phy, ele = 0, 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 邪渊之钩
            if opnt.status['torn'] + opnt.status['torn_buf_2'] > 0:     # 对方有撕裂状态，或对方比科斯魔速度快且撕裂状态下回合消失
                ele = 3 * 4
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("科斯魔发动技能[邪渊之钩]")
            for i in range(4):  # 4次攻击分开打印
                phy = random.randint(11, 22)
                print("科斯魔对" + opnt.name, end="")
                opnt.suffer(self, physical=phy)
            if ele > 0:
                print(opnt.name + "处于撕裂状态，科斯魔对" + opnt.name, end="")
                opnt.suffer(self, elemental=ele)
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['silenced'] == 0:  # 未被沉默
            # 普攻时15%概率，主动技能时1-(85%)^4=47.799375%
            if act == 1 and random.random() < 0.15 or act == 2 and random.random() < 0.47799375:
                print("科斯魔技能[不归之爪]触发，" + opnt.name + "陷入撕裂状态")
                if self.speed > opnt.speed:
                    opnt.status['torn_buf_1'] = 1
                else:
                    opnt.status['torn'] = 3
        # 状态更新
        self.status_change(act)
