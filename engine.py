import random

def get_next_state(game_map, current_state, action):
    if current_state not in game_map:
        return None
    
    if action in game_map[current_state]:
        result = game_map[current_state][action]
        
        if isinstance(result, list):
            return random.choice(result)
        else:
            return result
        
    else:
        return None
    
def battle():
    player_hp = 20
    monster_hp = 15
    
    while player_hp > 0 and monster_hp > 0:
        
        player_damage = random.randint(3,7)
        monster_damage = random.randint(2,6)
        
        print("\nCurrent HP")
        print(f"Player: {player_hp}, Monster: {monster_hp}")
        
        print(f"\nYou attacked a monster({player_damage} damage)")
        monster_hp -= player_damage
        if monster_hp <= 0:
            return "treasure"
        
        print(f"\nYou were attacked by a monster({monster_damage} damage)")
        player_hp -= monster_damage
        if player_hp <= 0:
            return "game_over"