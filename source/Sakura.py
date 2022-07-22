from hero import Hero


class Sakura(Hero):
    """
    生命: 100; 攻击: 24; 防御: 10; 速度: 27
    主动技能(夏之型·瓜切): 每2回合发动，回复自身1~5点生命值(最多回复至100点)，并对对手造成1.3倍自身攻击力的伤害(倍数伤害不计算小数点之后的数值)
    被动技能(夏之型·樱流): 受到攻击时有15%的概率闪避本回合所有攻击(不受沉默影响，无法闪避状态伤害)
    """

    def __init__(self, h=100, a=24, d=10, sp=27):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新