import random
from hero import Hero


class Aponia(Hero):
    """
    阿波尼亚
    生命: 100; 攻击: 21; 防御: 10; 速度: 30
    主动技能(深蓝之槛): 每4回合发动，对对手造成1.7倍自身攻击力的伤害(倍数伤害不计算小数点以后的数值)，并封印对方在本回合的行动
    被动技能(该休息了): 每次攻击有30%的概率沉默对手(本回合内主被动均失效，只能使用普通攻击，特殊标注除外)(混乱状态下触发时状态返还自身)
    """

    def __init__(self, h=100, a=21, d=10, sp=30):
        super().__init__(h, a, d, sp)
        self.name = "阿波尼亚"

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 4)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            print("阿波尼亚对" + opnt.name + "普攻，", end="")
            phy = self.attack
        elif act == 2:  # 深蓝之槛
            print("阿波尼亚发动技能[深蓝之槛]")
            print("阿波尼亚对" + opnt.name, end="")
            phy = int(self.attack * 1.7)
            opnt.status['skip'] = 1
        # 伤害结算
        if self.status['chaos'] == 1 and act == 1:   # 混乱
            self.suffer(phy)
        else:
            opnt.suffer(phy)
        # 被动判定
        if self.status['skip'] + self.status['silenced'] == 0:  # 不被跳过、沉默
            if act != 0:  # 自身攻击过
                if random.randint(1, 10) <= 3:  # 30%概率
                    if self.status['chaos'] == 1:   # 混乱状态
                        print("阿波尼亚被沉默，本回合无法使用技能")
                        self.status['silenced'] = 1
                    else:
                        print(opnt.name + "被沉默，本回合无法使用技能")
                        opnt.status['silenced'] = 1
        # 状态更新
        self.status_change(act)