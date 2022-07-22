import random

from hero import Hero


class Kevin(Hero):
    """
    生命: 100; 攻击: 20; 防御: 11; 速度: 21
    主动技能(清凉一剑): 每3回合发动，永久提升自身5点攻击力并对对方造成25点元素伤害
    被动技能(炎热归零): 攻击后有30%概率秒杀血量低于30%的对手(混乱状态触发时此技能不会触发)
    """
    def __init__(self, h=100, a=20, d=11, sp=21):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算
        phy, ele = 0, 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 清凉一剑
            self.attack += 5
            ele = 25
        # 伤害结算
        if self.status['chaos'] == 1 and act == 0:   # 混乱
            self.suffer(phy, ele)
        else:
            opnt.suffer(phy, ele)
        # 被动判定
        if self.status['skip'] + self.status['silenced'] + self.status['chaos'] == 0:   # 不被跳过、沉默、混乱
            if act != 0 and opnt.health <= 30:  # 自身攻击过、对方血量低于30%
                if random.randint(1, 10) <= 3:  # 30%概率
                    opnt.suffer(elemental=999)  # 其实不太严谨，没考虑华和格蕾修，但是够用了
        # 状态更新
        self.status_change(act)
