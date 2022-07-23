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

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新