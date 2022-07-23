import random

from hero import Hero


class Griseo(Hero):
    """
    格蕾修
    生命: 100; 攻击: 16; 防御: 11; 速度: 18
    主动技能(水彩泡影): 每3回合发动，绘制一个可以抵挡15点伤害的护盾，护盾受到伤害破碎时对对手造成自身防御力×200%~400%的伤害，护盾未破碎的情况下重新释放技能获得护盾时对对手造成自身防御力的伤害
    被动技能(沙滩监护人): 每次行动时有40%的概率永久提升自身2点防御力(最高获得10点)(沉默或无法行动时不会触发)
    """

    def __init__(self, h=100, a=16, d=11, sp=18):
        super().__init__(h, a, d, sp)
        self.name = "格蕾修"
        self.shield = 0     # 护盾值
        self.defence_plus = 0   # 额外防御力

    def suffer(self, opnt, physical=0, elemental=0, loss=0):
        """
        格蕾修护盾通过重构suffer函数实现
        """
        if self.shield == 0:    # 无盾
            super(Griseo, self).suffer(opnt, physical, elemental, loss)
            return
        # 物理伤害结算
        if physical > 0:
            damage = physical - self.defence
            if damage < 0:  # 伤害小于自身防御
                damage = 0
            if damage < self.shield:    # 未破盾
                self.shield -= damage
                print("造成0点伤害，格蕾修剩余生命值" + str(self.health) + "，剩余护盾" + str(self.shield))
            else:   # 破盾
                damage -= self.shield
                self.shield = 0
                self.health -= damage
                if self.health < 0:
                    self.health = 0
                print("造成" + str(damage) + "点伤害，格蕾修剩余生命值" + str(self.health) + "，护盾破碎")
                thorn = int(self.defence * random.randint(200, 400) / 100)
                print("格蕾修护盾碎裂，对" + opnt.name, end="")
                opnt.suffer(self, physical=thorn)
        # 元素伤害结算
        if elemental > 0:
            if elemental < self.shield:  # 未破盾
                self.shield -= elemental
                print("造成0点元素伤害，格蕾修剩余生命值" + str(self.health) + "，剩余护盾" + str(self.shield))
            else:  # 破盾
                elemental -= self.shield
                self.shield = 0
                self.health -= elemental
                if self.health < 0:
                    self.health = 0
                print("造成" + str(elemental) + "点伤害，格蕾修剩余生命值" + str(self.health) + "，护盾破碎")
                thorn = int(self.defence * random.randint(200, 400) / 100)
                print("格蕾修护盾碎裂，对" + opnt.name, end="")
                opnt.suffer(self, physical=thorn)
        # 生命流失结算，穿盾
        if loss > 0:
            super(Griseo, self).suffer(opnt, loss=loss)

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算
        phy, shd= 0, 0
        if act == 1:    # 普通攻击
            print("格蕾修对" + opnt.name + "普攻，", end="")
            phy = self.attack
        elif act == 2:
            print("格蕾修发动技能[水彩泡影]")
            print("格蕾修获得一个15生命值的护盾")
            shd = self.defence
        # 伤害结算
        if act == 1:
            if self.status['chaos'] == 1:
                print("格蕾修对格蕾修", end="")
                self.suffer(opnt, phy)  # 格蕾修由于混乱打破自己盾时，盾反伤害应该给对方
            else:
                opnt.suffer(self, phy)
        elif act == 2:
            if self.shield > 0:     # 护盾重叠
                print("格蕾修护盾重叠，对" + opnt.name, end="")
                opnt.suffer(self, physical=shd)
            self.shield = 15    # 无论是否重叠，重置为15
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['skip'] + self.status['silenced'] == 0:  # 不被跳过、沉默
            if self.defence_plus < 10:  # 最高获得10点
                if random.randint(1, 5) <= 2:   # 40%概率
                    self.defence += 2
                    self.defence_plus += 2
                    print("格蕾修发动技能[沙滩监护人]")
                    print("格蕾修防御提升2点，当前防御：" + str(self.defence))
        # 状态更新
        self.status_change(act)