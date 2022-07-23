from hero import Hero


class Eden(Hero):
    """
    伊甸
    生命: 100; 攻击: 16; 防御: 12; 速度: 16
    主动技能(闪亮登场): 每2回合发动，永久提升自身4点攻击力，对对手发动一次普通攻击(可触发被动技能)并使下回合先攻改为自己
    被动技能(海边协奏): 每次攻击有50%概率额外发动一次普通攻击，此技能每回合最多触发一次
    """

    def __init__(self, h=100, a=16, d=12, sp=16):
        super().__init__(h, a, d, sp)
        self.name = "伊甸"

    def action(self, turns, opnt):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 3)
        # 伤害计算

        # 伤害结算

        # 状态更新