class Game:
    board = []
    edges_board = []
    horizontal_edges = []
    vertical_edges = []
    scores = []
    current_player = 0
    players = []

    def __init__(self, M=4, N=4):
        self.M = M
        self.N = N

    def run(self, players):
        # create an empty game board
        self.edges_board = [[0 for _ in range(self.M - 1)] for _ in range(self.N - 1)]
        self.board = [[-1 for _ in range(self.M - 1)] for _ in range(self.N - 1)]
        self.horizontal_edges = [[False for _ in range(self.M - 1)] for _ in range(self.N)]
        self.vertical_edges = [[False for _ in range(self.M)] for _ in range(self.N - 1)]

        # create variables to track the current player and their score
        self.current_player = 0
        self.players = players
        self.scores = [0] * len(self.players)

        # create a loop that continues until the game is over
        while not self.is_game_finished():
            self.print_board()
            self.print_move()
            i, j, direction = self.players[self.current_player].make_move(self)
            if direction == -1:
                continue
            self.update_board(i, j, direction)

        self.print_board()
        self.print_scores()
        self.print_winner()

    def is_game_finished(self):
        all_verticals = all(all(line) for line in self.vertical_edges)
        all_horizontals = all(all(line) for line in self.horizontal_edges)
        return all_verticals and all_horizontals

    def update_board(self, i, j, direction):
        if direction == 'h':
            self.horizontal_edges[i][j] = True
        elif direction == 'v':
            self.vertical_edges[i][j] = True
        if not self._update_scores(i, j, direction):
            self.next_player()

    def _update_scores(self, i, j, direction):
        # check for completed squares
        scored = False
        if direction == 'h':
            if i > 0:
                self.edges_board[i - 1][j] += 1
                if self.edges_board[i - 1][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i - 1][j] = self.current_player
            if i < self.N - 1:
                self.edges_board[i][j] += 1
                if self.edges_board[i][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j] = self.current_player
        else:
            if j > 0:
                self.edges_board[i][j - 1] += 1
                if self.edges_board[i][j - 1] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j - 1] = self.current_player
            if j < self.M - 1:
                self.edges_board[i][j] += 1
                if self.edges_board[i][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j] = self.current_player
        return scored

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def print_board(self):
        # print the current state of the game board
        for i in range(self.N):
            print('.' + '.'.join(['-' if self.horizontal_edges[i][j] else ' ' for j in range(self.M - 1)]) + '.')
            if i < self.N - 1:
                print(''.join([('|' if self.vertical_edges[i][j] else ' ') + "{:1s}".format(
                    self._player_symbol(self.board[i][j]) if j < self.M - 1 else "") for j in range(self.M)]))

    def _player_symbol(self, player):
        if player == -1:
            return ' '
        return self.players[player].name[0]

    def print_move(self):
        print(f'{self.players[self.current_player].name} turn')

    def print_scores(self):
        print('Scores: ', end="")
        print(', '.join([f'{self.players[i].name} = {self.scores[i]}' for i in range(len(self.players))]))

    def print_winner(self):
        winner = self.better_player()
        if winner == -1:
            print("Game is over! It's draw")
        else:
            print(f'Game is over! The winner is player {self.players[winner].name}.')

    def better_player(self):
        first, second = sorted(((val, i) for i, val in enumerate(self.scores)), reverse=True)[:2]
        if first[0] == second[0]:
            return -1
        return first[1]

    def find_3_square_edge(self):
        for i in range(self.N - 1):
            for j in range(self.M - 1):
                if self.edges_board[i][j] == 3:
                    return self.find_edge_on_square(i, j)
        return 0, 0, -1

    def find_2_square_edge_shortest_chain(self):
        chains = self.find_chains()

        if len(chains) == 0:
            return 0, 0, -1

        shortest_chain = chains[0]
        square = shortest_chain[0]
        edge = self.find_edge_on_square(square[0], square[1])
        return edge

    def find_chains(self):
        chains = []

        check_board = [[False for _ in range(self.M - 1)] for _ in range(self.N - 1)]
        q = [(i, j) for j in range(self.M - 1) for i in range(self.N - 1)]

        while len(q) > 0:
            (i, j) = q.pop(len(q) - 1)

            def visit_2_square(k, l):
                if not (0 <= k < self.N - 1 and 0 <= l < self.M - 1):
                    return []
                if check_board[i][j] or self.edges_board[i][j] != 2:
                    return []
                check_board[k][l] = True
                yielder = self.edge_yielder(k, l)
                square_1 = next(yielder)
                square_2 = next(yielder)
                chain_1 = visit_2_square(square_1[0], square_1[1])
                chain_2 = visit_2_square(square_2[0], square_2[1])
                return chain_1 + [(k, l)] + chain_2

            chain = visit_2_square(i, j)
            if len(chain) > 0:
                chains.append(chain)

        chains = [(len(chain), chain) for chain in chains]
        chains.sort()
        chains = [chain for _, chain in chains]
        return chains

    def find_not_2_square_edge(self):
        for i in range(self.N - 1):
            for j in range(self.M - 1):
                if self.edges_board[i][j] < 2:
                    return self.find_edge_on_square(i, j)
        return 0, 0, -1

    def find_any_edge(self):
        for i in range(self.N - 1):
            for j in range(self.M - 1):
                if self.edges_board[i][j] < 4:
                    return self.find_edge_on_square(i, j)
        return 0, 0, -1

    def find_edge_on_square(self, i, j):
        if not self.horizontal_edges[i][j]:
            return i, j, 'h'
        if not self.horizontal_edges[i + 1][j]:
            return i + 1, j, 'h'
        if not self.vertical_edges[i][j]:
            return i, j, 'v'
        if not self.vertical_edges[i][j + 1]:
            return i, j + 1, 'v'
        return 0, 0, -1

    def edge_yielder(self, i, j):
        if not self.horizontal_edges[i][j]:
            yield i - 1, j
        if not self.horizontal_edges[i + 1][j]:
            yield i + 1, j
        if not self.vertical_edges[i][j]:
            yield i, j - 1
        if not self.vertical_edges[i][j + 1]:
            yield i, j + 1
        yield -1, -1

    def is_valid_move(self, i, j, direction):
        if direction == 'h':
            if i >= self.N or j >= self.M - 1:
                return False
            if self.horizontal_edges[i][j]:
                return False
        elif direction == 'v':
            if i >= self.N - 1 or j >= self.M:
                return False
            if self.vertical_edges[i][j]:
                return False
        else:
            return False
        return True
