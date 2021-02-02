from player import Person
from game import Game
from board import Board


def main():
    # Creates Two Player's
    player1 = Person("Me", "X")
    player2 = Person("You", "O")

    # Display Board
    Board.display_board()

    # Starts Game Loop
    Game(Board)

    count = 10
    while True:
        if count >= 0 and count % 2 == 0:
            move_request = int(input(f'Where would you like to place a {player1.token}?:  '))
            Game.move(move_request, player1.token)
            Game.is_full()
            Game.calc_winner()
            return True
        elif count >= 0 and count % 2 != 0:
            move_request = int(input(f'Where would you like to place a {player2.token}?:  '))
            Game.move(move_request, player2.token)
            return True
        else:
            return False


if __name__ == "__main__":
    main()
