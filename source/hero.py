import logging

logging.basicConfig(level=logging.INFO, format='%(massage)s')


class Hero(object):
    """
    英桀的基类，定义基本属性和基本框架
    """
    def __init__(self, h=0, a=0, d=0, sp=0):
        self.name = ""
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
        self.status.update({'sealed': 0})       # 跳过(阿波尼亚): 本回合不进行任何行动
        self.status.update({'stunned': 0})      # 昏迷(梅比乌斯): 下次无法行动
        self.status.update({'silenced': 0})     # 沉默(阿波尼亚): 本回合内主被动均失效，只能使用普通攻击，特殊标注除外
        self.status.update({'chaos': 0})        # 混乱(维尔薇): 下次普通攻击伤害返还自身，无视回合数
        self.status.update({'torn': 0})         # 撕裂(科斯魔): 每回合减少4点生命值，持续3回合，重复触发刷新状态，混乱状态下触发时状态返还自身
        self.status.update({'torn_buf_1': 0})   # 撕裂缓冲1(科斯魔): 科斯魔比对方速度快时，先附加这个状态，对方行动时将其转为撕裂，下回合对方行动时再造成伤害
        self.status.update({'torn_buf_2': 0})   # 撕裂缓冲2(科斯魔): 科斯魔比对方慢时，撕裂第3回合结束时，将撕裂转为缓冲2，科斯魔本回合释放技能时可触发元素伤害，下回合时再消除
        self.status.update({'charge': 0})       # 蓄力(华): 本回合不进行攻击，自身至下次行动前防御力提升3点，下次攻击时额外造成10~33点元素伤害(此伤害不受混乱状态影响)
        self.status.update({'miss': 0})         # 闪避(樱): 闪避本回合所有攻击
        self.status.update({'rest': 0})         # 休息(千劫): 本回合不进行任何行动

    def suffer(self, opnt, physical=0, elemental=0):
        """
        角色受到伤害(通用)，华、樱和格蕾修不适用
        :param physical: 物理伤害，需要经过防御减免
        :param elemental: 元素伤害，不受防御减免
        :return: 实际造成的伤害
        """
        # 物理伤害结算
        if physical > 0:
            damage = physical - self.defence
            if damage < 0:  # 伤害小于自身防御
                damage = 0
            self.health -= damage
            if self.health <= 0:
                self.health = 0
            print("造成" + str(damage) + "点伤害，" + self.name + "剩余生命值" + str(self.health))
            return damage
        # 元素伤害结算
        if elemental > 0:
            self.health -= elemental
            if self.health <= 0:
                self.health = 0
            print("造成" + str(elemental) + "点元素伤害，" + self.name + "剩余生命值" + str(self.health))
            return elemental

    def bleed(self, loss):
        """
        角色生命流失，即撕裂状态或千劫主动技能，有日志输出
        :param loss: 生命流失，不受防御减免，不可被闪避，不可被护盾抵挡
        """
        self.health -= loss
        if self.health <= 0:
            self.health = 0
        print(self.name + "生命值减少" + str(loss) + "，当前生命值" + str(self.health))

    def heal(self, val):
        """
        角色受到治疗，有日志输出
        :param val: 治疗值
        :return: 无
        """
        self.health += val
        if self.health > 100:
            self.health = 100
        print(self.name + "回复" + str(val) + "点生命值，当前生命值" + str(self.health))

    def execute(self):
        """
        凯文的秒杀效果，有日志输出
        """
        self.health = 0
        print("凯文对" + self.name + "造成999点元素伤害，" + self.name + "剩余生命值0")

    def basic_attack(self, opnt, phy):
        """
        普通攻击，考虑混乱状态的影响，有日志输出
        :param opnt: 对手
        :param phy: 普通攻击伤害
        :return: 实际造成的伤害，对自己造成伤害时为负数
        """
        print(self.name + "对" + opnt.name + "普攻，", end="")
        if self.status['chaos'] == 1:
            print("混乱状态生效，" + self.name + "对" + self.name, end="")
            self.status['chaos'] = 0
            return -1 * self.suffer(opnt, physical=phy)     # 此处填opnt是为了保证格蕾修自己破自己盾时，盾反伤害给对方(其实除了格蕾修没人需要看伤害来源)
        else:
            return opnt.suffer(self, physical=phy)

    def action(self, turns, opnt):
        """
        角色在本回合可以进行的操作，包括状态结算、普通攻击、主动技能、被动技能
        :param turns: 当前回合数
        :param opnt: 对手的实例化对象
        """
        pass

    def status_effect(self):
        """
        计算角色在本回合由于状态受到的影响，仅包括数值变化，不包括行动变化
        """
        if self.status['weak'] == 1:
            self.attack -= 6
        if self.status['torn'] > 0:
            print("[不归之爪]效果发动，", end="")
            self.bleed(4)
        if self.status['torn_buf_2'] == 1:  # 此时应该是撕裂状态消失后的第一个回合
            self.status['torn_buf_2'] = 0

    def decide_action(self, turns, cd):
        """
        判定角色在本回合的行动
        :param turns: 当前回合数
        :param cd: 角色主动技能冷却时间
        :return: 角色本回合的实际行动; 0->无行动, 1->普通攻击, 2->主动技能
        """
        if self.health == 0:    # 角色行动前已经战败
            return 0
        if self.status['sealed'] == 1:    # 封印
            print(self.name + "本回合无法行动")
            return 0
        elif self.status['stunned'] == 1:   # 昏迷
            print(self.name + "昏迷了")
            return 0
        elif self.status['rest'] == 1:  # 休息
            return 0
        elif self.status['silenced'] == 1:  # 沉默
            return 1
        elif turns % cd == 0:    # 主动技能
            if self.name == "千劫" and self.health < 11:  # 千劫特判：血量不足
                return 1
            return 2
        else:
            return 1

    def status_change(self, action):
        """
        计算角色在本回合结束时，状态层数的变化
        :param action: 角色本回合的实际行动
        """
        if self.status['weak'] == 1:
            self.attack += 6    # 无论如何，回合开始时减少的攻击力要加回来
            if action != 0:     # 如果本回合行动了，可以把状态清除
                self.status['weak'] = 0
        if self.status['torn'] > 0:
            self.status['torn'] -= 1
            if self.status['torn'] == 0 and self.speed > 19:    # 下回合撕裂状态消失，且对方比科斯魔速度快，将torn转为torn_buf_2
                self.status['torn_buf_2'] = 1   # 硬编码科斯魔速度，实现得比较烂，但凑合能用
        if self.status['miss'] == 1:
            self.status['miss'] = 0
        if self.status['sealed'] == 1:
            self.status['sealed'] = 0
        if self.status['stunned'] == 1:
            self.status['stunned'] = 0
        if self.status['silenced'] == 1:
            self.status['silenced'] = 0
        if self.status['rest'] == 1 and action == 0:    # 处于休息状态且本回合未行动(而不是施放主动技能)
            self.status['rest'] = 0
        if self.status['torn_buf_1'] == 1:    # 自身速度比科斯魔慢，本回合自身行动结束时，将torn_buf_1转为torn，下回合进入撕裂状态
            self.status['torn_buf_1'] = 0
            self.status['torn'] = 3
