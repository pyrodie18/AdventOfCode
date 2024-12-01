class move():
    def __init__(self):
        self.cost = 0
        self.damage = 0
        self.armor = 0
        self.heal = 0
        self.rounds = 0
        self.recharge = 0
        self.remaining = 0  # HOw many rounds are left for the active event
    
    def stats(self):
        return {
            "cost": self.cost,
            "boss_damage": self.damage,
            "armor": self.armor,
            "heal": self.heal,
            "recharge": self.recharge,
            "remaining": self.remaining            
        }
        
    def get_cost(self):
        return self.cost
    
    def start(self):
        self.remaining = self.rounds
        return self.cost, 0, 0
    
    def use(self):
        self.remaining -= 1
        
    def active(self):
        if self.remaining > 0:
            return self.cost
        else:
            return 0
        
class missle(move):
    def __init__(self):
        super().__init__()
        self.cost = 53
        self.damage = 4
        
    def start(self):
        return self.cost, 4, 0
        
class drain(move):
    def __init__(self):
        super().__init__()
        self.cost = 73
        self.damage = 2
        self.heal = 2
    
    def start(self):
        return self.cost, 2, 2
        
class shield(move):
    def __init__(self):
        super().__init__()
        self.cost = 113
        self.armor = 7
        self.rounds = 6
        
class poison(move):
    def __init__(self):
        super().__init__()
        self.cost = 173
        self.rounds = 6
        self.damage = 3
        
class recharge(move):
    def __init__(self):
        super().__init__()
        self.cost = 229
        self.rounds = 5
        self.recharge = 229
        
MOVES = {
    "missle": missle(),
    "drain": drain(),
    "shield": shield(),
    "poison": poison(),
    "recharge": recharge()
    }

def calculate_move():
    armor = 0
    boss_damage = 0
    healing = 0
    recharge = 0
    
    # Use each of the current spells
    for i in MOVES.keys():
        tmp = MOVES[i].stats()
        if tmp["remaining"] > 0:
            boss_damage += tmp["boss_damage"]
            armor += tmp["armor"]
            healing += tmp["heal"]
            recharge += tmp["recharge"]
            MOVES[i].use()
    return armor, boss_damage, healing, recharge 

def play_game():
    import random
    
    my_ph = 50
    my_mana = 500
    boss_ph = 51
    boss_attack = 9
    spent = 0
    history = []
    
    while my_ph > 0 and boss_ph > 0:
        armor, boss_damage, healing, recharge = calculate_move()
        boss_ph -= boss_damage
        my_ph += healing
        my_mana += recharge
        
        # See if the boss is dead
        if boss_ph <= 0:
            return spent
        
        possible_moves = [ i for i in MOVES.keys() if MOVES[i].active() < my_mana ]
        if len(possible_moves) > 0:
            move = random.choice(possible_moves)
            history.append(move)
            cost, boss_damage, healing = MOVES[move].start()
            spent += cost
            my_mana -= cost
            boss_ph -= boss_damage
            my_ph += healing
            
        armor, boss_damage, healing, recharge = calculate_move()
        boss_ph -= boss_damage
        my_ph += healing
        my_mana += recharge
        
        if boss_ph <= 0:
            return spent
        
        my_ph -= (max(1, (boss_attack - armor)))
        if my_ph <= 0:
            return 0

def part1():
    low_score = 1000000000
    for i in range(1000):
        score = play_game()
        if score > 0:
            low_score = min(low_score, score)

    
    print('Part 1:  {}'.format(str(low_score)))

def part2():
    answer = None
    # print('Part 2:  {}'.format(str(answer)))

part1()
# part2()
