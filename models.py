from dataclasses import dataclass, field
from rich.console import Console
console = Console()
@dataclass()
class Player:
    name: str
    numbers: list = field(default_factory=list)
    iswinner: bool = False

@dataclass()
class Board:
    positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    def draw(self, positions = positions):
        console.print(f" {self.positions[0]} [bold green]|[/bold green] {self.positions[1]} [bold green]|[/bold green] {self.positions[2]}")
        console.print("---+---+---", style="bold green")
        console.print(f" {self.positions[3]} [bold green]|[/bold green] {self.positions[4]} [bold green]|[/bold green] {self.positions[5]}")
        console.print("---+---+---", style="bold green")
        console.print(f" {self.positions[6]} [bold green]|[/bold green] {self.positions[7]} [bold green]|[/bold green] {self.positions[8]}\n")
    def board_fill(self, xo, playerX, playerO):
        for x in xo:
            if x in playerX:
                self.positions[x - 1] = "X"
            elif x in playerO:
                self.positions[x - 1] = "O"
        print("\n")