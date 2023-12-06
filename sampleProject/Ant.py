from MobileCritter import MobileCritter
from Insect import Insect


class Ant(Insect, MobileCritter):

    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this ant's position 1 unit right"""
        self.position[0] += 1
        # todo
        #raise NotImplementedError()

    def move_left(self):
        """moves this ant's position 1 unit left"""
        # todo
        self.position[0] -=1
        #raise NotImplementedError()

    def move_up(self):
        """moves this ant's position 2 units up"""
        self.position[1] +=2
        # todo
        #raise NotImplementedError()

    def move_down(self):
        """moves this ant's position 2 units down"""
        self.position [1] -=2
        # todo
        #raise NotImplementedError()

    def __str__(self):
        return u'\u1F41C'
