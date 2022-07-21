from hero import Hero


class Mobius(Hero):
    """
    生命: 100; 攻击: 21; 防御: 11; 速度: 23
    主动技能(栖影水枪): 每3回合发动，对对手造成33点伤害并有33%的概率使对手陷入昏迷状态(无法行动)至对手下次行动阶段结束
    被动技能(不稳定物质): 普通攻击造成伤害时有33%的概率使对手陷入腐蚀状态，防御力永久下降3点，最多下降至0点(混乱状态下触发时状态返还自身)
    """

    def __init__(self, h=100, a=21, d=11, sp=23):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算

        # 角色行动

        # 状态更新