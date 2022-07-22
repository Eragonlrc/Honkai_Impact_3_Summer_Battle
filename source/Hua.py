from hero import Hero


class Hua(Hero):
    """
    生命: 100; 攻击: 21; 防御: 12; 速度: 15
    主动技能(上伞若水): 每2回合发动，进入蓄力状态，本回合不进行攻击，自身至下次行动前防御力提升3点，下次攻击时额外对对手造成10~33点元素伤害(此伤害不受混乱状态影响)
    被动技能(攻守兼备): 受到的伤害减少20%(不受沉默状态影响)
    """

    def __init__(self, h=100, a=21, d=12, sp=15):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新