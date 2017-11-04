
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 8, Python game of Pig, with computer player"""

from random import randint

def player_factory(name, player_type):
    """
    Creates a player/computer given a type
    :param name: player name, player type
    :param player_type: "H" for human, "C" for computer
    :return: roll, score
    """
    if player_type == 'H':
        return Player(name)
    elif player_type == 'C':
        return ComputerPlayer(name)


class Player(object):
    raw_input("New Pig Game - Press Enter to Begin")
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self, timed='n'):
        self.timed = timed
        print "----------------------------------------------------------"
        print "Player", self.name, "begin"
        print "Current score is {}".format(self.score)
        while True:
            myroll = randint(1, 6)
            print " you got a", myroll
            if myroll == 1:
                self.score = 0
                print " your score is", self.score
                break
            else:
                self.score += myroll
                print " your score is", self.score
                if self.score >= 100:
                    return
                ans = raw_input("do you want to continue (y=yes n=no)?")
                if ans == 'n':
                    break

        print "next player"


class ComputerPlayer(Player):

    def play(self):
        print "----------------------------------------------------------"
        print "Player", self.name, "begin"
        print "Current score is {}".format(self.score)
        while True:
            myroll = randint(1, 6)
            print " you got a", myroll

            if myroll == 1:
                self.score = 0
                print " your score is", self.score
                break
            else:
                self.score += myroll
                print " your score is", self.score
                if self.score < 25 and self.score < (100-self.score):
                    continue
                else:
                    break

        print "next player"

class TimedGameProxy(Player):
    """timed game of pig"""
    def __init__(self):
        self.start = time.time()
        Player.__init__(self, 'player1, player2')

    def timer(self):
        p1=player_factory("Al", "H")
        p2 = player_factory("PC Becca", 'C')

        if self.timed == 'y':

            while time.time() - self.start >= 60 and p1.score < 100 and p2.score < 100:
                p1.play()
                if p1.score >= 100:
                    print "{} wins".format(p1.name)
                    break
                p2.play()
                if p2.score >= 100:
                    print "{} wins".format(p2.name)
                    break
                if time.time() - self.start >= 60:
                    if pl.score > p2.score:
                        print "Game over, Player1 wins"
                    elif p2.score > p1.score:
                        print "Game over, Player1 wins"
                    elif p1.score == p2.score:
                        print "Game over, TIE GAME"


def main():
    p1 = player_factory("Al", "H")
    p2 = player_factory("PC Becca", 'C')
    while p1.score < 100 and p2.score < 100:
        p1.play()
        if p1.score >= 100:
            print "{} wins".format(p1.name)
            break
        p2.play()
        if p2.score >= 100:
            print "{} wins".format(p2.name)
            break
            

if __name__ == "__main__":
    main()

