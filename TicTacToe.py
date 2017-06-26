'''
Time complexity: O(N^3)
'''

class TicTacToe:
    # Players Actions
    O = 'O'
    X = 'X'

    # Constructor
    def __init__(self, n):
        self.n = n
        self.remaining_moves = self.n*self.n
        self.game_board = [[i+self.n*(j)+1 for i in range(self.n)] for j in range(self.n)]
        self.player1_name = None
        self.player2_name = None

    # Game main function
    def game_play(self):

        self.player1_name = input("Enter name for Player 1: ")
        self.player2_name = input("Enter name for Player 2: ")
        self.game_board_print()

        # While no winner or remaining moves is greater than 0
        while True:

            player1_move = None
            # Validate player input
            while player1_move is None:
                player1_move = input(self.player1_name + ", choose a box to place an 'X' into: ")
                player1_move = self.game_input_validate(player1_move, self.X)

            self.game_board_print()
            # Check if X is a winner
            if self.game_checker('X'):
                print("Congratulations " + self.player1_name +"! You have won.")
                break
            if self.remaining_moves <= 0:
                print("No winner for this game!")
                break

            player2_move = None
            # Validate player input
            while player2_move is None:
                player2_move = input(self.player2_name + ", choose a box to place an 'O' into: ")
                player2_move = self.game_input_validate(player2_move, self.O)

            self.game_board_print()
            # Check if O is a winner
            if self.game_checker('O'):
                print("Congratulations " + self.player2_name + "! You have won.")
                break
            if self.remaining_moves <= 0:
                print("No winner for this game!")
                break

    """
    Time Complexity: O(N^2)
    """
    def game_checker(self, player_handel):

        # Check vertical
        for i in range(self.n):
            squares = 0
            for j in range(self.n):
                if self.game_board[i][j] == player_handel:
                    squares += 1
                else:
                    squares = 0

                if squares == 3:
                    return True

        # Check horizontal
        for i in range(self.n):
            squares = 0
            for j in range(self.n):
                if self.game_board[j][i] == player_handel:
                    squares += 1
                else:
                    squares = 0

                if squares == 3:
                    return True

        # Check top-left to bottom-right
        squares = 0
        for i in range(self.n):
            if self.game_board[i][i] == player_handel:
                squares += 1
            else:
                squares = 0

            if squares == 3:
                return True

        # Check top-right to bottom-left
        squares = 0
        for i in range(self.n):
            if self.game_board[i][self.n-i-1] == player_handel:
                squares += 1
            else:
                squares = 0

            if squares == 3:
                return True

        return False

    def game_input_validate(self, player_move, player_handel):
        try:
            user_input = int(player_move)
        except ValueError:
            print("Please enter a valid move!")
            return None

        if user_input <= 0 or user_input > self.n * self.n:
            print("Please enter a valid move! <1 to " + str(self.n * self.n) + ">")
            return None

        user_input -= 1
        x = int(user_input / self.n)
        y = int(user_input % self.n)

        if self.game_board[x][y] == self.X or self.game_board[x][y] == self.O:
            print("Spot already taken, please enter a valid move!")
            return None

        self.game_board[x][y] = player_handel
        self.remaining_moves -= 1

        return user_input

    def game_board_print(self):
        print('\n'.join([''.join(['{:4}|'.format(str(item)) for item in row]) for row in self.game_board]))
        print('\n')

try:
    n = int(input("Please enter board dimension: "))
    if n < 3 or n > 20:
        raise ValueError

    tto = TicTacToe(n)
    tto.game_play()

except ValueError:
    print("Please enter a valid dimension <3 to 20>!")


