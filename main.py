from models import Player, Board
import pyinputplus as pyip
from rich.console import Console

lucky = [[1, 2, 3,], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
console = Console()

def luck_check(player, lucky=lucky):
    for lucky_set in lucky:
        checker = 0
        for arg in lucky_set:
            if arg in player.numbers:
                checker += 1
                if checker == 3:
                    player.iswinner = True
                    console.print(f"[bold blue]{player.name}[/bold blue] wins!", style="bold green")
                    return False
                pass

def get_num(player):
    while True:
        try:
            console.print(f"[bold blue]{player.name}[/bold blue] turn: ", style="bold green")
            num = int(input())
            if num < 0 or num > 9:
                console.print("Number is not on the board!", style="bold red")
                continue
            if num in all_numbers:
                console.print("This field is taken!", style="bold red")
                continue
            all_numbers.append(num)
            return num
        except ValueError:
            console.print("Your choice is not a number!", style="bold red")

def play():
    game_board = Board
    game_board.positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    game_board.draw(game_board, all_numbers)
    all_numbers.clear()
    player_x.numbers = []
    player_o.numbers = []
    player_x.iswinner = False
    player_o.iswinner = False
    console.print("\n\n\n\n\nThis is 'Tic Tac Toe' game. You know the rules.\n", style="bold blue")
    while not player_x.iswinner or player_o.iswinner:
        if len(all_numbers) == 9: break
        for plr in players:
            if len(all_numbers) == 9:
                console.print("Draw!", style="bold cyan")
                break
            plr.numbers.append(get_num(plr))
            print("\n" * 10)
            game_board.board_fill(game_board, all_numbers, player_x.numbers, player_o.numbers)
            game_board.draw(game_board)
            luck_check(plr)
            if plr.iswinner: break

player_x = Player("Player X")
player_o = Player("Player O")
players = [player_x, player_o]
all_numbers = []


if __name__ == "__main__":
    while True:
        print("\n")
        console.print("1 - Start game", style="bold blue")
        console.print("2 - Exit", style="bold blue")
        menu = input()
        match menu:
            case "1":
                play()
            case "2":
                console.print("Exiting the game. Goodbye!", style="bold red")
                break
            case _:
                console.print("Invalid option. Please try again.", style="bold red")
