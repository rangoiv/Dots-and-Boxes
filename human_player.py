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
        if not self.is_valid_move(game, i, j, direction):
            return 0, 0, -1
        return i, j, direction

    def is_valid_move(self, game, i, j, direction):
        if direction == 'h':
            if i >= game.N or j >= game.M - 1:
                print('Invalid edge! Please try again.')
                return False
            if game.horizontal_edges[i][j]:
                print('The edge is already taken! Please try again.')
                return False
        elif direction == 'v':
            if i >= game.N - 1 or j >= game.M:
                print('Invalid edge! Please try again.')
                return False
            if game.vertical_edges[i][j]:
                print('The edge is already taken! Please try again.')
                return False
        else:
            print('Invalid direction! Please try again.')
            return False
        return True
