from hero import Hero


class Pardofelis(Hero):
    """
    生命: 100; 攻击: 17; 防御: 10; 速度: 24
    主动技能(沙滩寻宝): 每3回合发动，对对手造成30点伤害并使自身回复实际造成伤害的生命值(生命值最多回复至100点)
    被动技能(最佳搭档): 每次攻击有30%概率召唤罐头，对对手造成30点伤害(罐头攻击不受混乱状态影响)
    """

    def __init__(self, h=100, a=17, d=10, sp=24):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新