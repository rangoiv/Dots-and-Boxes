from player import Player


class HumanPlayer(Player):
    def make_move(self, game):
        game.print_board()
        # prompt the current player for their move
        edge = input(f'Player {self.player_name}, enter your edge: ')

        # parse the move and update the game board
        try:
            j, i, direction = edge.split()
            i, j = int(i), int(j)
        except ValueError:
            print('Invalid move! Please type: "i j dir".')
            return 0, 0, -1
        if not game.is_valid_move(i, j, direction):
            return 0, 0, -1
        return i, j, direction


