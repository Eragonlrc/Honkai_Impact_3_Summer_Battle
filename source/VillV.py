from hero import Hero


class VillV(Hero):
    """
    维尔薇
    生命: 100; 攻击: 20; 防御: 12; 速度: 25
    主动技能(创(造)力): 每3回合发动，对对手造成自己攻击力的伤害，并使对手陷入混乱状态(效果：对手下次普通攻击伤害返还自身，无视回合数)
    被动技能(大变活人): 回合开始时若维尔薇血量低于31，则自身与对手回复10~20点生命值(生命值回复分别计算)，并永久提升自身2~15点攻击力(每场比赛最多触发1次)
    """

    def __init__(self, h=100, a=20, d=12, sp=25):
        super().__init__(h, a, d, sp)
        self.name = "维尔薇"

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新