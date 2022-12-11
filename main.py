LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

# define the number dot rows
N = 2
# define the number dot columns
M = 3
# define the players
players = ['X', 'O']
is_AI = [0, 0]


class Game:
    board = []
    horizontal_edges = []
    vertical_edges = []
    scores = []

    def run(self):

        # create an empty game board
        self.board = [[' ' for _ in range(M - 1)] for _ in range(N - 1)]
        self.horizontal_edges = [[False for _ in range(M - 1)] for _ in range(N)]
        self.vertical_edges = [[False for _ in range(M)] for _ in range(N - 1)]

        # create variables to track the current player and their score
        current_player = 0
        self.scores = [0, 0]

        # create a loop that continues until the game is over
        while True:
            self.print_board()

            # prompt the current player for their move
            edge = input(f'Player {players[current_player]}, enter your edge: ')

            # parse the move and update the game board
            try:
                i, j, direction = edge.split()
                i, j = int(i), int(j)
            except ValueError:
                print('Invalid edge! Please type: "i j s".')
                continue
            if not self.is_good_move(i, j, direction):
                print('Invalid Move!')
                continue

            self.make_move(i, j, direction)

            # check for completed squares
            if direction == 'h':
                if (i > 0 and self.horizontal_edges[i - 1][j] and
                        self.vertical_edges[i - 1][j] and self.vertical_edges[i - 1][j + 1]):
                    self.board[i - 1][j] = players[current_player]
                    self.scores[current_player] += 1
                if (i < N - 1 and self.horizontal_edges[i + 1][j] and
                        self.vertical_edges[i][j] and self.vertical_edges[i][j + 1]):
                    self.board[i][j] = players[current_player]
                    self.scores[current_player] += 1
            else:
                if (j > 0 and self.vertical_edges[i][j - 1] and
                        self.horizontal_edges[i][j - 1] and self.horizontal_edges[i + 1][j - 1]):
                    self.board[i][j - 1] = players[current_player]
                    self.scores[current_player] += 1
                if (j < M - 1 and self.vertical_edges[i][j + 1] and
                        self.horizontal_edges[i][j] and self.horizontal_edges[i + 1][j + 1]):
                    self.board[i][j] = players[current_player]
                    self.scores[current_player] += 1

            current_player = (current_player + 1) % len(players)

    def is_good_move(self, i, j, direction):
        if direction == 'h':
            if i >= N or j >= M - 1 or self.horizontal_edges[i][j]:
                print('Invalid edge! Please try again.')
                return False
        elif direction == 'v':
            if i >= N - 1 or j >= M or self.vertical_edges[i][j]:
                print('Invalid edge! Please try again.')
                return False
        else:
            print('Invalid edge! Please try again.')
            return False
        return True

    def make_move(self, i, j, direction):
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

game = Game()
game.run()
