import random
from hero import Hero


class Kevin(Hero):
    """
    凯文
    生命: 100; 攻击: 20; 防御: 11; 速度: 21
    主动技能(清凉一剑): 每3回合发动，永久提升自身5点攻击力并对对方造成25点元素伤害
    被动技能(炎热归零): 攻击后有30%概率秒杀血量低于30%的对手(混乱状态触发时此技能不会触发)
    """
    def __init__(self, h=100, a=20, d=11, sp=21):
        super().__init__(h, a, d, sp)
        self.name = "凯文"

    def action(self, turns, opnt: Hero):
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
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("凯文发动技能[清凉一剑]")
            print("凯文攻击力提升5点，当前攻击力" + str(self.attack))
            print("凯文对" + opnt.name, end="")
            opnt.suffer(self, elemental=ele)
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['sealed'] + self.status['stunned'] + self.status['silenced'] + self.status['chaos'] == 0:    # 不被封印、昏迷、沉默、混乱
            if opnt.health <= 30:  # 对方血量低于30%
                if random.random() < 0.3:  # 30%概率
                    print("凯文发动技能[炎热归零]")
                    opnt.execute()
        # 状态更新
        self.status_change(act)
