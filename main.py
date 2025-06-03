from models import Player, Board
lucky = [[1, 2, 3,], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def luck_check(player, lucky=lucky):
    for lucky_set in lucky:
        checker = 0
        for arg in lucky_set:
            if arg in player.numbers:
                checker += 1
                if checker == 3:
                    player.status = True
                    print(f"{player.name} wins!")
                pass

def get_num(player):
    while True:
        try:
            num = int(input(f"{player.name} turn: "))
            if num < 0 or num > 9:
                print("Number is not on the board!")
                continue
            if num in all_numbers:
                print("This field is taken!")
                continue
            all_numbers.append(num)
            return num
        except ValueError:
            print("Your choice is not a number!")
        # except Exception as e:
            # match e:
            #     case ValueError():
            #         print("Your choice is not a number!")

player_x = Player("Player X")
player_o = Player("Player O")
players = [player_x, player_o]
all_numbers = []
game_board = Board

print("This is 'Tic Tac Toe' game. You know the rules.")

while not player_x.status or player_o.status:
    for plr in players:
        plr.numbers.append(get_num(plr))
        print("\n" * 10)
        game_board.board_fill(game_board, all_numbers)
        game_board.draw(game_board)
        luck_check(plr)
        if plr.status: break

