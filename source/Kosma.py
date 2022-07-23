from hero import Hero


class Kosma(Hero):
    """
    科斯魔
    生命: 100; 攻击:19; 防御: 11; 速度: 19
    主动技能(邪渊之钩): 每2回合发动，对对手造成4次攻击，每次攻击造成11~22点伤害，若对手处于撕裂状态，则每次攻击会额外附加3点元素伤害
    被动技能(不归之爪): 每次攻击结束有15%概率使对手陷入撕裂状态，从下回合开始每回合减少4点生命值，持续3回合，重复触发刷新状态(混乱状态下触发时状态返还自身)
    """

    def __init__(self, h=100, a=19, d=11, sp=19):
        super().__init__(h, a, d, sp)
        self.name = "科斯魔"

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新