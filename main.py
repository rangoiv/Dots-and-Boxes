from game import Game
from minimax_player import MinimaxPlayer
from simple_player import SimplePlayer
from human_player import HumanPlayer


def main():
    players = [SimplePlayer("Sparkles"), MinimaxPlayer("Minimax", d=7)]
    game = Game(4, 4)
    game.run(players)


if __name__ == '__main__':
    main()
