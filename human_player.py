from player import Player


class HumanPlayer(Player):
    def make_move(self, game):
        # prompt the current player for their move
        edge = input('Enter your move: ')

        # parse the move and update the game board
        try:
            j, i, direction = edge.split()
            i, j = int(i), int(j)
        except ValueError:
            print('Invalid move! Please enter: "x y dir".')
            return 0, 0, -1
        if not game.is_valid_move(i, j, direction):
            print('Invalid move! Please enter: "x y dir".')
            return 0, 0, -1
        return i, j, direction


