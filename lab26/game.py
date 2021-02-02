from board import Board

class Game:
    count = 9

    def __init__(self, board):
        self.board = board

    def __repr__(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def move(self, move_request: int, player: str):
        # move_request = int(input(f'Where would you like to place a {player.id}?:  '))
        count = 9

        while count <= 0:
            if self.board[move_request] is None:
                self.board[move_request] = player.token
                count -= 1
                return
            elif self.board[move_request] is not None:
                move_request = int(input('The space on the board isn\'t available, please choose again.'))
                return move_request

    def calc_winner(self) -> bool:
        if self.board[0] == self.board[1] == self.board[2]:
            return True
        elif self.board[3] == self.board[4] == self.board[5]:
            return True
        elif self.board[6] == self.board[7] == self.board[8]:
            return True
        elif self.board[0] == self.board[3] == self.board[6]:
            return True
        elif self.board[0] == self.board[4] == self.board[8]:
            return True
        elif self.board[1] == self.board[4] == self.board[7]:
            return True
        elif self.board[2] == self.board[5] == self.board[8]:
            return True
        else:
            return False

    def is_full(self) -> bool:
        while True:
            for spaces in self.board:
                if self.board[spaces] is None:
                    return True
                else:
                    print("The board is full, no more available spaces!")
                    return False

    def is_game_over() -> bool:
        if self.count == 0:
            return True
        else:
            self.count -= 1
            return False
