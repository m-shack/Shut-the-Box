"""Shut the Box Game by Mark Shackelford."""
# Updated on 7/5/15 with PEP8 using Atom editor.
# test 

import random
from itertools import chain, combinations


class Die(object):

    """Simulate a 6-sided die."""

    def __init__(self):
        """Define a die."""
        self.roll()

    def roll(self):
        """Update the die with a random roll."""
        self.value = random.randint(1, 6)
        return self.value

    def get_value(self):
        """Return the value set by last roll()."""
        return self.value

    def set_value_0(self):
        """Set the value to 0. Used for rolls requiring only one die."""
        self.value = 0


class Dice(object):

    """Simulate a pair of dice."""

    def __init__(self, n=2):
        """Create the two Die objects."""
        self.myDice = [Die(), Die()]
        if n == 1:
            self.myDice[1].set_value_0()

    def roll(self):
        """Return a random roll of the dice."""
        for d in self.myDice:
            d.roll()

    def get_total(self):
        """Get total of two dice."""
        t = 0
        for d in self.myDice:
            t += d.get_value()
        return t

    def get_list(self):
        """Return a list of the Die values."""
        return [d.get_value() for d in self.myDice]


class Box(object):

    """Simulate the box including 9 numbered tiles."""

    def __init__(self):
        """Define the Box."""
        self.tiles = list(range(1, 10))
        self.options = [1]
        self.dice = Dice()

    def subsets(self, s):
        """Define the possible subsets."""
        def powerset(iterable):
            """Powerset([1,2,3]) ->(1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)."""
            s = list(iterable)
            return chain.from_iterable(combinations(s, r)
                                       for r in range(len(s)+1))
        return map(set, powerset(s))

    def play_one_turn(self):
        """Sequence of events to play a turn."""
        if sum(self.tiles) < 7:
            self.dice = Dice(1)
        else:
            self.dice.roll()
        self.options = [list(s) for s in self.subsets(self.tiles) if
                        sum(s) == self.dice.get_total()]
        if self.options:
            print()
            for index, value in enumerate(self.options):
                print(index, value)
            print("\nRemaining tiles: {0:35} Your roll: {1}\n".format
                  (str(self.tiles), str(self.dice.get_list())))
            while True:
                choice = input('Enter your choice: ')
                if choice == "":
                    choice = '0'
                if choice.isdigit():
                    choice = int(choice)
                    break
            for i in self.options[choice]:
                self.tiles.remove(i)
            print("Updated tile list:", str(self.tiles))
        else:
            print("Last roll:", str(self.dice.get_list()))

    def get_score(self):
        """Calculate and display the score."""
        # use map and join to create score string
        score = "Your Score: {:,}".format(int(''.join(map(str, self.tiles))))
        return score


def main():
    """Main function for Shut the Box game."""
    while True:
        box1 = Box()
        while box1.tiles and box1.options:
            box1.play_one_turn()
        if box1.tiles:
            print('\n{0} \n'.format(box1.get_score()))
        else:
            print("\nCongratulations - YOU SHUT THE BOX!!!!\n")
        if input("Enter Q to Quit: ").upper() == "Q":
            break
    print("\nbye\n\n")

if __name__ == '__main__':
    main()
