from hero import Hero


class Kalpas(Hero):
    """
    生命: 100; 攻击: 23; 防御: 9; 速度: 26
    主动技能(盛夏燔祭): 每3回合发动，燃烧自己10点生命值，对对手造成45点伤害并附加1~20点元素伤害，此后休息一回合(血量不足11点时无法发动)
    被动技能(夏之狂热): 生命值越低攻击力越高，每损失5点生命值提高1点攻击力(每次行动时触发)(不受沉默效果影响)
    """

    def __init__(self, h=100, a=23, d=9, sp=26):
        super().__init__(h, a, d, sp)

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新