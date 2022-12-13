from game import Game
from minimax_player import MinimaxPlayer
from simple_player import SimplePlayer
from human_player import HumanPlayer


def main():
    players = [MinimaxPlayer("Minimax1", 0), MinimaxPlayer("Minimax", 1)]
    game = Game()
    game.run(players)


if __name__ == '__main__':
    main()
