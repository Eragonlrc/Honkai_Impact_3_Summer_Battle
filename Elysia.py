from hero import Hero


class Elysia(Hero):
    """
    生命: 100; 攻击: 21; 防御: 8; 速度: 20
    主动技能(夏梦之花): 每2回合发动，对对手造成25~50点伤害并使对手下次行动时攻击力下降6点(行动不包括释放被动技能)
    被动技能(水花溅射): 攻击后有35%概率追加一次溅射攻击，造成11点元素伤害(混乱状态下触发时伤害返还给自身)
    """

    def __init__(self, h=100, a=21, d=8, sp=20):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算

        # 角色行动

        # 状态更新
