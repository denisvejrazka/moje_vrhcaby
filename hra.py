import random
''''
povinně implementovaná funkčnost:
    generování hodu kostkami
    výpis všech možných tahů hráče
    jednoduchá umělá inteligence, která náhodně volí jeden z platných tahů
    trasování chodu každého jednotlivého kamene (od vstupu z baru po vyhození/vyvedení), herní pole se chovají jako zásobník
    uložení a obnova stavu hry (s návrhem vlastního JSON formátu pro uložení)
'''
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Board:
    def __init__(self):
        self.bar = Bar()
        self.home = Home()
        self.points = [Point() for _ in range(24)]
        self.players = [Player("Player 1", "●"), Player("Player 2", "○")]
        self.current_player = random.choice(self.players)
        self.dice = Dice()

    def print_board(self):
        ...


class Dice:
    def __init__(self):
        self.values = []

    def throw(self):
        self.values = [random.randint(1, 6), random.randint(1, 6)]
        return self.values

class Stone:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

class Point:
    def __init__(self):
        self.stones = []

    def __str__(self):
        return ", ".join(str(stone) for stone in self.stones)

    def add_stone(self, player):
        self.stones.append(Stone(player.color))

    def remove_stone(self):
        return self.stones.pop()

    def check_valid_move(self, player, roll1, roll2):
        return True

class Dice:
    def __init__(self):
        self.values = []
    
    def throw(self):
        values = [random.randint(1,6), random.randint(1,6)]
        return values
    
class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = [(x, y)]  

    def move_stone(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.positions.append((new_x, new_y))  

    def history(self):
        return self.positions 

class Bar:
    def __init__(self) -> None:
        pass

class Home:
    def __init__(self) -> None:
        pass

dice = Dice()
board = Board()

