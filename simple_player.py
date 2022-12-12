from player import Player


class SimplePlayer(Player):
    def make_move(self, game):
        i, j, direction = game.find_3_square_edge()
        if direction == -1:
            i, j, direction = game.find_not_2_square_edge()
        if direction == -1:
            i, j, direction = game.find_2_square_edge_shortest_chain()
        return i, j, direction
