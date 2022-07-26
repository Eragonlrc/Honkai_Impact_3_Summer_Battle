import random
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

    def action(self, turns, opnt: Hero):
        # 状态结算
        self.status_effect()
        # 行动判定
        act = self.decide_action(turns, 2)
        # 伤害计算
        phy = 0
        if act == 1:    # 普通攻击
            phy = self.attack
        elif act == 2:  # 闪亮登场
            self.attack += 4
            phy = self.attack
            self.speed = 99
        # 伤害结算
        if act == 1:
            self.basic_attack(opnt, phy)
        elif act == 2:
            print("伊甸发动技能[闪亮登场]")
            print("伊甸攻击力永久提升4点，当前攻击力" + str(self.attack))
            print("下回合伊甸先攻")
            self.basic_attack(opnt, phy)
        if opnt.health == 0:    # 对方战败
            return
        # 被动判定
        if self.status['sealed'] + self.status['stunned'] + self.status['silenced'] == 0:  # 不被封印、昏迷、沉默
            if random.random() < 0.5:   # 50%概率
                print("伊甸发动技能[海边协奏]")
                print("伊甸对" + opnt.name + "追加一次普攻，", end="")
                if self.status['weak'] == 1:    # 特殊情况：伊甸的追加攻击不受爱莉希雅的虚弱影响
                    phy += 6
                if self.status['chaos'] == 1:   # 由于文本不同，不能调basic_attack
                    print("混乱状态生效，伊甸对伊甸", end="")
                    self.suffer(self, physical=phy)
                    self.status['chaos'] = 0
                else:
                    opnt.suffer(self, physical=phy)
        # 状态更新
        self.status_change(act)
