import random

monsters = {
    "slime": {
        "hp": 10,
        "min_dmg": 1,
        "max_dmg": 4
    },
    "goblin": {
        "hp": 15,
        "min_dmg": 2,
        "max_dmg": 6
    },
    "dragon": {
        "hp": 25,
        "min_dmg": 4,
        "max_dmg": 10
    }
}

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
    
def battle(player):
    monster_name = random.choice(list(monsters.keys()))
    monster = monsters[monster_name]
    monster_hp = monster["hp"]
    
    print(f"\nA wild {monster_name} appeared!")
    
    while player["hp"] > 0 and monster_hp > 0:
        
        player_damage, p_cri = calculate_damage(3,7)
        monster_damage, m_cri = calculate_damage(
            monster["min_dmg"],
            monster["max_dmg"]
        )
        
        print("\nCurrent HP")
        print(f"Player: {player['hp']}, Monster: {monster_hp}")
        
        print("\nYou attacked a monster")
        if p_cri:
            print(f"Critical Hit! {player_damage} damage!")
        else:
            print(f"{player_damage} damage")
        monster_hp -= player_damage
        if monster_hp <= 0:
            return "treasure"
            
        print("\nYou were attacked by a monster")
        if m_cri:
            print(f"Critical Hit! {monster_damage} damage!")
        else:
            print(f"{monster_damage} damage")
        player['hp'] -= monster_damage
        if player['hp'] <= 0:
            return "game_over"
        
def calculate_damage(min_dmg, max_dmg):
    is_critical = False
    critical_rate = 0.9
    damage = random.randint(min_dmg, max_dmg)
    
    if random.random() <= critical_rate:
        is_critical = True
        damage *= 2
        return damage, is_critical
    
    else:
        return damage, is_critical