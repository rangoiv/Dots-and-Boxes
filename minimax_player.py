import copy

from player import Player


class MinimaxPlayer(Player):
    def __init__(self, player_name, maximize_player, d=3):
        super().__init__(player_name)
        self.maximize_player = maximize_player
        self.d = d

    def make_move(self, game):
        initial_state = GameState(game)
        alpha = -float('inf')
        beta = float('inf')
        _, move = minimax(initial_state, self.d, alpha, beta, self.maximize_player)
        return move


def minimax(state, depth, alpha, beta, maximize_player):
    if depth == 0 or state.is_terminal():
        return state.evaluate(), state.last_move

    if state.game.current_player == maximize_player:
        best_value = -float('inf')
        best_move = state.last_move
        for child in state.get_children():
            value, move = minimax(child, depth - 1, alpha, beta, False)
            best_value, best_move = (value, move) if best_value < value else (best_value, move)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value, best_move
    else:
        best_value = float('inf')
        best_move = state.last_move
        for child in state.get_children():
            value, move = minimax(child, depth - 1, alpha, beta, True)
            best_value, best_move = (value, move) if best_value > value else (best_value, move)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_move


class GameState:
    def __init__(self, game, last_move=(0, 0, -1)):
        self.game = copy.deepcopy(game)
        self.last_move = last_move
        pass

    def is_terminal(self):
        return self.game.is_game_finished()

    def get_children(self):
        # Return a list of all possible subsequent states
        states = []
        for i in range(len(self.game.horizontal_edges)):
            for j in range(len(self.game.horizontal_edges[0])):
                if not self.game.horizontal_edges[i][j]:
                    state = GameState(self.game, (i, j, 'h'))
                    state.game.update_board(i, j, 'h')
                    states.append(state)

        for i in range(len(self.game.vertical_edges)):
            for j in range(len(self.game.vertical_edges[0])):
                if not self.game.vertical_edges[i][j]:
                    state = GameState(self.game, (i, j, 'v'))
                    state.game.update_board(i, j, 'v')
                    states.append(state)
        return states

    def evaluate(self):
        # Return a numeric value representing the value of the current state
        scores = self.game.scores.copy()
        current_player_score = scores.pop(self.game.current_player)
        max_other_player_score = max(scores)
        max_scores = (self.game.N - 1) * (self.game.M - 1)
        if current_player_score > max_scores/2:
            return float('inf')
        if max_other_player_score > max_scores/2:
            return -float('inf')
        return current_player_score - max_other_player_score
