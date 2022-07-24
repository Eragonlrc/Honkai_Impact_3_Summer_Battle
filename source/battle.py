from hero import Hero


class Battle(object):
    """
    一局比赛
    """
    def __init__(self, p1: Hero, p2: Hero):
        self.turn = 0
        self.winner = 0
        self.player1 = p1
        self.player2 = p2

    def run(self):
        if self.player1.speed < self.player2.speed:     # 设定保证无相同速度的英桀
            self.player1, self.player2 = self.player2, self.player1     # player1先攻
        print("回合0")
        print("战斗开始，{0}对战{1}，{0}先手".format(self.player1.name, self.player2.name))
        while True:
            self.turn += 1
            print("回合"+str(self.turn))
            self.player1.action(self.turn, self.player2)
            if self.player2.health == 0:
                self.winner = self.player1
                break
            elif self.player1.health == 0:
                self.winner = self.player2
                break
            self.player2.action(self.turn, self.player1)
            if self.player1.health == 0:
                self.winner = self.player2
                break
            elif self.player2.health == 0:
                self.winner = self.player1
                break

        print(self.winner.name + "获得了胜利")
