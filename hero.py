class Hero:
    """
    英桀的基类，定义基本属性和基本框架
    """
    def __init__(self, h=0, a=0, d=0, sp=0):
        self.health = h
        self.attack = a
        self.defence = d
        self.speed = sp
        self.status = {}
        self.init_status()

    def init_status(self):
        """
        所有状态的初始化，用字典{名称, 层数}存储
        """
        self.status.update({'weak': 0})         # 虚弱(爱莉希雅): 下次行动时攻击力下降6点，行动不包括释放被动技能
        self.status.update({'sealed': 0})       # 封印(阿波尼亚): 本回合不进行任何行动
        self.status.update({'silenced': 0})     # 沉默(阿波尼亚): 本回合内主被动均失效，只能使用普通攻击，特殊标注除外
        self.status.update({'chaos': 0})        # 混乱(维尔薇): 下次普通攻击伤害返还自身，无视回合数
        self.status.update({'rest': 0})         # 休息(千劫): 本回合不进行任何行动
        self.status.update({'torn': 0})         # 撕裂(科斯魔): 每回合减少4点生命值，持续3回合，重复触发刷新状态，混乱状态下触发时状态返还自身
        self.status.update({'stunned': 0})      # 昏迷(梅比乌斯): 无法行动，至下次行动阶段结束
        self.status.update({'shield': 0})       # 护盾(格蕾修): 抵挡伤害
        self.status.update({'accumulate': 0})   # 蓄力(华): 本回合不进行攻击，自身至下次行动前防御力提升3点，下次攻击时额外造成10~33点元素伤害(此伤害不受混乱状态影响)

    def suffer(self, physical=0, elemental=0, loss=0):
        """
        角色受到伤害
        :param physical: 物理伤害，需要经过防御减免
        :param elemental: 元素伤害，不受防御减免
        :param loss: 生命流失，不受防御减免
        :return: 角色是否死亡
        """
        # 物理伤害结算
        self.health -= physical - self.defence
        if self.health <= 0:
            self.health = 0
            return True
        # 元素伤害结算
        self.health -= elemental
        if self.health <= 0:
            self.health = 0
            return True
        # 生命流失结算
        self.health -= loss
        if self.health <= 0:
            self.health = 0
            return True
        return False

    def heal(self, val):
        """
        角色受到治疗
        :param val: 治疗值
        :return: 无
        """
        self.health += val
        if self.health > 100:
            self.health = 100

    def action(self):
        """
        角色在本回合可以进行的操作，包括状态结算、普通攻击、主动技能、被动技能
        """
        pass
