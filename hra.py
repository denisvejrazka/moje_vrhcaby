import random
# TO DO:
# JSON

class Bar:
    def __init__(self):
        self.bar_stones = []
        self.free_back_in_game_positions = []

    def add_stone_to_bar(self, position):
        self.bar_stones.append(board.board[position].stones[0])
        board.board[position].remove_stone()
        print(f"Hráč na pozici {position} byl vyhozen!")

    def remove_stone_from_bar(self):
        self.bar_stones.pop()

    def count_stones_for_player(self, player):
        count = sum(1 for stone in self.bar_stones if stone.owner == player)
        return count
    
    def back_to_board_position_counter(self, player):
        for value in [dice.values[0], dice.values[1], (dice.values[0]+dice.values[1])]:
            if not board.board[1+value].stones or (board.board[1+value].stones[0].owner != player and len(board.board[1+value].stones) == 1) or board.board[1+value].stones[0].owner == player:
                if value in range(1,7):
                    self.free_back_in_game_positions.append(value)
                elif value in range(18, 25):
                    self.free_back_in_game_positions.append(24-value)
        print(self.free_back_in_game_positions)

    def back_in_game(self, player):
        if player.from_pos in self.free_back_in_game_positions:
            return True
        else:
            return False
        
    def out_of_game(self):
        if len(board.board[game.current_player.to_pos].stones) == 1 and board.board[game.current_player.from_pos].stones[0].owner != board.board[game.current_player.to_pos].stones[0].owner: 
            bar.add_stone_to_bar(game.current_player.to_pos)
            board.board[game.current_player.to_pos].add_stone(game.current_stone)
            return True
        return False    

    def check_if_player_able_to_play(self, player, stone):
        for s in bar.bar_stones:
            if s.owner == player and bar.bar_stones.count(stone) > 0:
                return False
        return True
            

class Player:
    def __init__(self, name, stone_symbol):
        self.name = name
        self.stone_symbol = stone_symbol
        self.on_turn = False
        self.from_pos = 0
        self.to_pos = 0
        self.home_tile = []
        self.free_positions = []
        self.home_tile_count = 0
        self.home = []

    def get_player_from(self):
        game.current_player.from_pos = int(input("Z jaké pozice chceš hrát? "))

    def get_player_to(self):
        game.current_player.to_pos = int(input("Na jakou pozici se chceš přesunout? "))

class Game:
    def __init__(self):
        self.is_game_over = False
        self.players = [player1, player2]
        self.current_player = None
        self.current_stone = None
        self.positions = []


    def greet(self):
        print("Ahoj, Vítej ve hře vrhcáby. Hra se hraje následovně... Vyber z které pozice na kterou se chceš přesunout.")

    def get_initial_player(self):
        self.current_player = random.choice(self.players)
        self.current_player.on_turn = True
        print(f"Začíná {self.current_player.name}.")

    def switch_player(self):
        if player1.on_turn:
            player1.on_turn = False
            player2.on_turn = True
            game.current_player = player2
        elif player2.on_turn:
            player2.on_turn = False
            player1.on_turn = True
            game.current_player = player1

    def get_current_stone(self):
        if game.current_player == player1:
            self.current_stone = stone1
        elif game.current_player == player2:
            self.current_stone = stone2

    def check_valid_move(self):
        #teoreticky nemusí být, protože se tah musí nacházet v možných pozicích (sekce pod tím)
        #kontrola pohybu pro hráče1
        for t in stone1.memory:
            for i in range(len(t)-1):
                if t[i] > t[i+1]:
                    print("Špatný směr pohybu")
                    return False
        #kontrola pohybu pro hráče2
        for t in stone2.memory:
            for i in range(len(t)-1):
                if t[i] < t[i+1]:
                    print("Špatný směr pohybu")
                    return False
           
        if player1 == game.current_player and player1.to_pos not in [player1.from_pos+dice.values[0], player1.from_pos+dice.values[1], player1.from_pos+(dice.values[0]+dice.values[1])]:
            print("Nevhodný tah")
            return False
        elif player2 == game.current_player and player2.to_pos not in [player2.from_pos-dice.values[0], player2.from_pos-dice.values[1], player2.from_pos-(dice.values[0]+dice.values[1])]:
            print("Nevhodný tah")
            return False
        return True
    
    def count_home_tile_stones(self, player, home_tile):
        for col in home_tile:
            for stone in col.stones:
                if stone.owner == player:
                    player.home_tile_count += 1
        if player.home_tile_count == 15:
            return True
        
    def check_wins(self):
        if len(player1.home) == 15:
            print(f"{player1.name} vyhrává!")
            return True
        elif len(player2.home) == 15:
            print(f"{player2.name} vyhrává!")
            return True
        return False

    def find_available_moves(self, free_positions):
        self.positions.clear()
        for pos in free_positions:
            if pos in range(24):
                if (len(board.board[pos].stones) >= 1 and board.board[pos].stones[0].owner == game.current_player) or (not board.board[pos].stones) or (len(board.board[pos].stones) == 1 and board.board[pos].stones[0].owner != game.current_player):
                    self.positions.append(pos)
            elif (pos in [24, 26]) or (pos in [0]):
                if game.count_home_tile_stones(game.current_player, game.current_player.home_tile):
                    self.positions.append(pos)
                
    def check_if_players_stone(self):
        #nepovoli hraci hrat za kamen, ktery neni jeho
        if board.board[game.current_player.from_pos].stones[0].owner != game.current_player:
            print("Nemůžete operovat s kameny druhého hráče!")
            return False 
    
    def detect_home_move(self):
        if game.current_player.to_pos == 25:
            player1.home.append(stone1)
        elif game.current_player.to_pos == 0:
            player2.home.append(stone2)

    def get_player_back_to_board(self):
        bar.back_to_board_position_counter(game.current_player)
        game.current_player.get_player_from()
        if bar.back_in_game(game.current_player):
            board.board[game.current_player.from_pos].add_stone(game.current_stone)
            bar.remove_stone_from_bar()
        else:
            print("Hráče nebylo možné dostat zpět do hry")
        game.switch_player()
  
#herní deska
class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(26)]

    def set_initial_board_layout(self):
        board.board[1].add_stone(stone2)
        board.board[1].add_stone(stone2)   
        board.board[6].add_stone(stone1)   
        board.board[6].add_stone(stone1)   
        board.board[6].add_stone(stone1)   
        board.board[6].add_stone(stone1)   
        board.board[6].add_stone(stone1)
        board.board[8].add_stone(stone1)   
        board.board[8].add_stone(stone1)   
        board.board[8].add_stone(stone1)   
        board.board[11].add_stone(stone1)   
        board.board[15].add_stone(stone1)   
        board.board[12].add_stone(stone2)   
        board.board[12].add_stone(stone2)   
        board.board[12].add_stone(stone2)   
        board.board[12].add_stone(stone2)   
        board.board[12].add_stone(stone2)   
        board.board[13].add_stone(stone1)   
        board.board[13].add_stone(stone1)   
        board.board[13].add_stone(stone1)   
        board.board[13].add_stone(stone1)   
        board.board[13].add_stone(stone1)   
        board.board[17].add_stone(stone2)   
        board.board[17].add_stone(stone2)   
        board.board[17].add_stone(stone2)   
        board.board[19].add_stone(stone2)   
        board.board[19].add_stone(stone2)   
        board.board[19].add_stone(stone2)   
        board.board[19].add_stone(stone2)   
        board.board[19].add_stone(stone2)   
        board.board[24].add_stone(stone1)   
        board.board[24].add_stone(stone1)     
        

    def print_board(self):
        print(f"   Aktuální počet {player2.stone_symbol} na baru: {bar.count_stones_for_player(player2)}     ○ Doma: {len(player2.home)}")
        #výpis pozic
        for i in range(12, 0, -1):
            #spacing
            print(f"{i:2}", end=" ")
        print()
        print("+" + "--+" * 11)                         

        for row in range(10): #prochází kameny (řádky)
            for i in range(12, 0, -1): #prochází sloupce
                if row < len(self.board[i].stones): #kontroluje, zda v dané pozici na desce je nějaký kámen, Pokud ano, vezme se kámen a zjistí se, komu patří a přiřadí se symbol hráče (player_stone_symbol)
                    stone = self.board[i].stones[row] #definice stone
                    player_stone_symbol = None
                    #rozpoznává, který stone symbol bude vytisknut
                    for player in game.players: 
                        if stone.owner == player: 
                            player_stone_symbol = player.stone_symbol
                    print(player_stone_symbol, end="  ") if player_stone_symbol else print("  ", end=" ")
                else:
                    # Prázdný prostor, pokud řádek neobsahuje kámen
                    print("  ", end=" ")
            print()

        for row in range(10, -1, -1):  # -1, protože chceme aby nahoře byl poslední daný kámen
            for i in range(13, 25):
                if row < len(self.board[i].stones):
                    stone = self.board[i].stones[row]
                    player_stone_symbol = None
                    for player in game.players:
                        if stone.owner == player:
                            player_stone_symbol = player.stone_symbol

                    print(player_stone_symbol, end="  ") if player_stone_symbol else print("  ", end=" ")
                else:
                    # Prázdný prostor, pokud řádek neobsahuje kámen
                    print("  ", end=" ")
            print()
        
        #výpis pozic
        print("+" + "--+" * 11)
        for i in range(13, 25, 1):
            print(f"{i:2}", end=" ")
        print()

        print(f"   Aktuální počet {player1.stone_symbol} na baru: {bar.count_stones_for_player(player1)}       ● Doma: {len(player1.home)}")

#kostka 
class Dice:
    def __init__(self):
        self.values = []

    def throw(self):
        self.values = [random.randint(1, 6), random.randint(1, 6)]
        return self.values

#kámen
class Stone:
    def __init__(self, player):
        self.memory = []
        self.owner = player
        self.from_pos = None
        self.to_pos = None
        self.symbol = player.stone_symbol

#Herní políčko
class Tile:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone: Stone):
        self.stones.append(stone) 
        if game.current_player == player1:
            stone1.memory.append((game.current_player.from_pos, game.current_player.to_pos))
        elif game.current_player == player2:
            stone2.memory.append((game.current_player.from_pos, game.current_player.to_pos))

    def remove_stone(self):
        self.stones.pop()

    def print_stones(self):
        print(self.stones)


# Inicializace hry / vytváření instancí
bar = Bar()
player1 = Player("Hráč 1", "●") # hráč začínající od zhora doleva
player2 = Player("Hráč 2", "○") # hráč začínající zespoda doleva
game = Game()
board = Board()
dice = Dice()
stone1 = Stone(player1)
stone2 = Stone(player2)
tile = Tile()


#inicialization
game.greet()
board.set_initial_board_layout()
player1.home_tile = board.board[19:]
player2.home_tile = board.board[:6]
#testing
game.get_initial_player()
while not game.check_wins():
    print(game.current_player.name)
    board.print_board()
    print(dice.throw())
    game.get_current_stone()
    if not bar.check_if_player_able_to_play(game.current_player, game.current_stone):
        game.get_player_back_to_board()
        continue
    game.current_player.get_player_from()
    game.check_if_players_stone()
    player1.free_positions = [player1.from_pos+dice.values[0], player1.from_pos+dice.values[1], player1.from_pos+(dice.values[0]+dice.values[1])]
    player2.free_positions = [player2.from_pos-dice.values[0], player2.from_pos-dice.values[1], player2.from_pos-(dice.values[0]+dice.values[1])]
    game.find_available_moves(game.current_player.free_positions)
    print(game.positions)
    game.current_player.get_player_to()
    game.detect_home_move()
    if game.current_player.to_pos == game.current_player.free_positions[2]:
        board.board[game.current_player.from_pos].remove_stone()
        board.board[game.current_player.to_pos].add_stone(game.current_stone)
        game.switch_player()
        continue
    if not bar.out_of_game():
        board.board[game.current_player.from_pos].remove_stone()
        board.board[game.current_player.to_pos].add_stone(game.current_stone)

    if not bar.check_if_player_able_to_play(game.current_player, game.current_stone):
        game.get_player_back_to_board()
        continue
    game.current_player.get_player_from()
    player1.free_positions = [player1.from_pos+dice.values[0], player1.from_pos+dice.values[1], player1.from_pos+(dice.values[0]+dice.values[1])]
    player2.free_positions = [player2.from_pos-dice.values[0], player2.from_pos-dice.values[1], player2.from_pos-(dice.values[0]+dice.values[1])]
    game.find_available_moves(game.current_player.free_positions)
    print(game.positions)
    game.current_player.get_player_to()
    game.detect_home_move()
    if not bar.out_of_game():
        board.board[game.current_player.from_pos].remove_stone()
        board.board[game.current_player.to_pos].add_stone(game.current_stone)

    game.switch_player()