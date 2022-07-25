import random
from hero import Hero


class Hua(Hero):
    """
    华
    生命: 100; 攻击: 21; 防御: 12; 速度: 15
    主动技能(上伞若水): 每2回合发动，进入蓄力状态，本回合不进行攻击，自身至下次行动前防御力提升3点，下次攻击时额外对对手造成10~33点元素伤害(此伤害不受混乱状态影响)
    被动技能(攻守兼备): 受到的伤害减少20%(不受沉默状态影响)
    """

    def __init__(self, h=100, a=21, d=12, sp=15):
        super().__init__(h, a, d, sp)
        self.name = "华"

    def suffer(self, opnt, physical=0, elemental=0):
        """
        华的被动技能通过重构suffer函数实现
        """
        # 物理伤害结算
        if physical > 0:
            damage = physical - self.defence
            damage = round(damage * 0.8)
            if damage < 0:  # 伤害小于自身防御
                damage = 0
            self.health -= damage
            if self.health <= 0:
                self.health = 0
            print("造成" + str(damage) + "点伤害，华剩余生命值" + str(self.health))
            return damage
        # 元素伤害结算
        if elemental > 0:
            elemental = round(elemental * 0.8)
            return super(Hua, self).suffer(opnt, elemental=elemental)

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 2)
        # 伤害计算
        phy, ele = 0, 0
        if act == 1:    # 普通攻击
            if self.status['charge'] == 1:  # 蓄力附加元素伤害
                ele = random.randint(10, 33)
            phy = self.attack
        elif act == 2:  # 上伞若水
            pass    # 无伤害
        # 伤害结算
        if act != 0 and self.status['charge'] == 1:     # 行动前消除蓄力状态
            self.status['charge'] = 0
            self.defence -= 3
        if act == 1:
            print("华对" + opnt.name + "普攻，", end="")
            if self.status['chaos'] == 1:
                print("混乱状态生效，华对华", end="")
                super(Hua, self).suffer(opnt, phy)    # 混乱状态下华对自己的伤害不受被动减免(很不合理，但确实如此)
            else:
                opnt.suffer(self, phy)
            if ele > 0 and self.status['silenced'] == 0:     # 此时蓄力状态已经消失，若ele>0则表明需要附加元素伤害；沉默时不附加伤害
                print("蓄力生效，华对" + opnt.name + "额外", end="")
                opnt.suffer(self, elemental=ele)    # 附加元素伤害不受混乱影响
        elif act == 2:
            print("华发动技能[上伞若水]")
            print("华至下次行动前防御力提升3点，", end="")
            self.status['charge'] = 1
            self.defence += 3
            print("当前防御" + str(self.defence))
        if opnt.health == 0:    # 对方战败
            return
        # 状态更新
        self.status_change(act)
