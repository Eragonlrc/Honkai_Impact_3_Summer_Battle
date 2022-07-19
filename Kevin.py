from hero import Hero


class Kevin(Hero):
    """
    生命: 100; 攻击: 20; 防御: 11; 速度: 21
    主动技能(清凉一剑): 每3回合发动，永久提升自身5点攻击力并对对方造成25点元素伤害
    被动技能(炎热归零): 攻击后有30%概率秒杀血量低于30%的对手(混乱状态触发时此技能不会触发)
    """
    def __init__(self, h=100, a=20, d=11, sp=21):
        super().__init__(h, a, d, sp)

    def action(self):
        #
