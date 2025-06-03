from dataclasses import dataclass, field
@dataclass()
class Player:
    name: str
    numbers: list = field(default_factory=list)
    status: bool = False

@dataclass()
class Board:
    positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    def draw(self, positions = positions):
        print(f" {self.positions[0]} | {self.positions[1]} | {self.positions[2]}")
        print("---+---+---")
        print(f" {self.positions[3]} | {self.positions[4]} | {self.positions[5]}")
        print("---+---+---")
        print(f" {self.positions[6]} | {self.positions[7]} | {self.positions[8]}")
    def board_fill(self, xo):
        for x in xo:
            self.positions[x - 1] = str(x)
