LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

# define the number dot rows
N = 4
# define the number dot columns
M = 4
# define the players
players = ['X', 'O']
is_AI = [1, 1]


class Game:
    board = []
    edges_board = []
    horizontal_edges = []
    vertical_edges = []
    scores = []
    current_player = 0

    def run(self):

        # create an empty game board
        self.edges_board = [[0 for _ in range(M - 1)] for _ in range(N - 1)]
        self.board = [[' ' for _ in range(M - 1)] for _ in range(N - 1)]
        self.horizontal_edges = [[False for _ in range(M - 1)] for _ in range(N)]
        self.vertical_edges = [[False for _ in range(M)] for _ in range(N - 1)]

        # create variables to track the current player and their score
        self.current_player = 0
        self.scores = [0] * len(players)

        # create a loop that continues until the game is over
        while True:
            if is_AI[self.current_player]:
                i, j, direction = self.make_move()
            else:
                self.print_board()
                i, j, direction = self.enter_move()
            if direction == -1:
                continue

            self.update_board(i, j, direction)
            if not self.update_scores(i, j, direction):
                self.next_player()
            if self.is_game_finished():
                print(f'Game is over! The winner is player {players[self.better_player()]}')
                self.print_board()
                break

    def enter_move(self):
        # prompt the current player for their move
        edge = input(f'Player {players[self.current_player]}, enter your edge: ')

        # parse the move and update the game board
        try:
            i, j, direction = edge.split()
            i, j = int(i), int(j)
        except ValueError:
            print('Invalid edge! Please type: "i j dir".')
            return 0, 0, -1
        if not self.is_good_move(i, j, direction):
            return 0, 0, -1
        return i, j, direction

    def is_good_move(self, i, j, direction):
        if direction == 'h':
            if i >= N or j >= M - 1:
                print('Invalid edge! Please try again.')
                return False
            if self.horizontal_edges[i][j]:
                print('The edge is already taken! Please try again.')
                return False
        elif direction == 'v':
            if i >= N - 1 or j >= M:
                print('Invalid edge! Please try again.')
                return False
            if self.vertical_edges[i][j]:
                print('The edge is already taken! Please try again.')
                return False
        else:
            print('Invalid direction! Please try again.')
            return False
        return True

    def make_move(self):
        i, j, direction = self.find_3_square_edge()
        if direction == -1:
            i, j, direction = self.find_not_2_square_edge()
        if direction == -1:
            i, j, direction = self.find_any_edge()
        return i, j, direction

    def find_3_square_edge(self):
        for i in range(N-1):
            for j in range(M-1):
                if self.edges_board[i][j] == 3:
                    return self.find_edge_on_square(i, j)
        return 0, 0, -1

    def find_not_2_square_edge(self):
        for i in range(N-1):
            for j in range(M-1):
                if self.edges_board[i][j] < 2:
                    return self.find_edge_on_square(i, j)
        return 0, 0, -1

    def find_any_edge(self):
        for i in range(N-1):
            for j in range(M-1):
                if self.edges_board[i][j] < 4:
                    return self.find_edge_on_square(i, j)

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

    def update_scores(self, i, j, direction):
        # check for completed squares
        scored = False
        if direction == 'h':
            if i > 0:
                self.edges_board[i - 1][j] += 1
                if self.edges_board[i - 1][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i - 1][j] = players[self.current_player]
            if i < N - 1:
                self.edges_board[i][j] += 1
                if self.edges_board[i][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j] = players[self.current_player]
        else:
            if j > 0:
                self.edges_board[i][j - 1] += 1
                if self.edges_board[i][j - 1] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j - 1] = players[self.current_player]
            if j < M - 1:
                self.edges_board[i][j] += 1
                if self.edges_board[i][j] == 4:
                    scored = True
                    self.scores[self.current_player] += 1
                    self.board[i][j] = players[self.current_player]
        return scored

    def update_board(self, i, j, direction):
        if direction == 'h':
            self.horizontal_edges[i][j] = True
        elif direction == 'v':
            self.vertical_edges[i][j] = True

    def print_board(self):
        # print the current state of the game board
        print(LINE_UP, LINE_UP, LINE_UP, LINE_UP)
        for i in range(N):
            print('.' + '.'.join(['-' if self.horizontal_edges[i][j] else ' ' for j in range(M - 1)]) + '.')
            if i < N - 1:
                print(''.join([('|' if self.vertical_edges[i][j] else ' ') + "{:1s}".format(
                    self.board[i][j] if j < M - 1 else "") for j in range(M)]))
        # print the current self.scores
        print(f'Scores: X={self.scores[0]}, O={self.scores[1]}')

    def is_game_finished(self):
        all_verticals = all(all(line) for line in self.vertical_edges)
        all_horizontals = all(all(line) for line in self.horizontal_edges)
        return all_verticals and all_horizontals

    def better_player(self):
        _, i = max((val, i) for i, val in enumerate(self.scores))
        return i

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(players)


game = Game()
game.run()
