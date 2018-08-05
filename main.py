#!/usr/bin/env python
"""Battleship is a two player games.
"""
import sys
import os
from random import randint


class Board:
    """This is a class for interaction with game"""
    ships = [[], []]
    shipSize = {1: 5, 2: 4, 3: 2, 5: 2}
    hits = [[], []]
    screen1 = ['~'] * 100
    screen2 = ['~'] * 100
    screen = [screen1, screen2]
    table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
             'G': 6, 'H': 7, 'I': 8, 'J': 9}

    def insert_ships(self, ships):
        """Randomly insert ships in the water"""
        for _ in range(ships):
            self.ships[0].append(randint(0, 99))
            self.ships[1].append(randint(0, 99))

    def game_reset(self, ships):
        """Resets the game"""
        self.ships = [[], []]
        self.insert_ships(ships)
        self.hits = [[], []]
        self.screen = [['~'] * 100, ['~'] * 100]

    def move(self, rows, column):
        """A lookup table for converting the rows and column to
        index"""
        return int(rows) * 10 + self.table[column]

    def draw(self):
        """Draws the game board"""
        print(" "*23+"BATTLESHIP")
        print("      player 1's board \t\t   player 2's board\n")
        print("    A B C D E F G H I J\t\t  A B C D E F G H I J")
        print("   ____________________\t\t ____________________")
        for i in range(10):
            ften = 0 + 10 * i
            lten = 10 + 10 * i
            print(str(i) + " | ", end='')
            print(' '.join(self.screen[0][ften:lten]), end=' ')
            print("\t" + "| ", end='')
            print(' '.join(self.screen[1][ften: lten]), end='\n')

    def win(self, player):
        """Checks if the player won"""
        for i in self.ships[player-1]:
            if i not in self.hits[player-1]:
                return 0
        return 1

    def winner(self):
        """Returns the winner"""
        if self.win(1) == 1:
            return 1
        elif self.win(2) == 1:
            return 2
        return 0

    def change_screen(self, player, position):
        """Prints the hits and misses"""
        if position in self.ships[player-1]:
            self.screen[player-1][position] = 'X'
        else:
            self.screen[player-1][position] = 'M'

    def valid_input(self):
        """Checks if the input is valid"""
        row = input("row\t= ")
        while row not in [str(z) for z in range(10)]:
            print("invalid input")
            row = input("row\t= ")

        column = input("column\t= ")
        while column.upper() not in self.table.keys():
            print("invalid input")
            column = input("column\t= ")
        return row, column

    def players_chance(self, player):
        """Player's chance"""
        row, column = self.valid_input()
        while self.move(row, column.upper()) in self.hits[player-1]:
            print('Move exists')
            row, column = self.valid_input()
        return row, column

    def game(self, ships):
        """Main game control"""
        self.game_reset(ships)
        player = 1
        while self.winner() == 0:
            os.system('clear')
            self.draw()
            print("Player %d's chance" % player)

            row, column = self.players_chance(player)

            self.hits[player-1].append(self.move(row, column.upper()))
            self.change_screen(player, self.move(row, column.upper()))

            player = 3-player


if __name__ == '__main__':
    try:
        SHIPS = int(sys.argv[1])
    except IndexError:
        SHIPS = 10

    if SHIPS not in range(1, 100):
        print("Not a valid number for ships")
        print("default of 10 ships considered")
        SHIPS = 10

    BOARD = Board()
    BOARD.game(SHIPS)
    print("The Winner is Player %d" % BOARD.winner())
    while input("Press 'enter' to restart and 'q' to quit:") != 'q':
        BOARD.game(SHIPS)
