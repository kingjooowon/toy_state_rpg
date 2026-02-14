import random

monsters = {
    "slime": {
        "hp": 10,
        "min_dmg": 1,
        "max_dmg": 4,
        "xp": 5,
        "weight": 50
    },
    "goblin": {
        "hp": 15,
        "min_dmg": 2,
        "max_dmg": 6,
        "xp": 10,
        "weight": 30
    },
    "dragon": {
        "hp": 25,
        "min_dmg": 4,
        "max_dmg": 10,
        "xp": 25,
        "weight": 10
    },
    "orc": {
        "hp": 30,
        "min_dmg": 2,
        "max_dmg": 5,
        "xp": 15,
        "weight": 20
    },
    "girl_friend": {
        "hp": 100,
        "min_dmg": 100,
        "max_dmg": 100,
        "xp": 1000,
        "weight": 1
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
    names = []
    weights = []
    
    for name, data in monsters.items():
        base = data['weight']
        
        if name == 'slime':
            scaled = max(5, base - player['level'] * 5)
        elif name == 'dragon':
            scaled = base + player['level'] * 5
        else:
            scaled = base + player['level'] * 2
            
        names.append(name)
        weights.append(scaled)
        
    monster_name = random.choices(names, weights=weights, k=1)[0]
    monster_data = monsters[monster_name]
    monster = monster_data.copy()

    print(f"\nA wild {monster_name} appeared!")
    
    while player["hp"] > 0 and monster['hp'] > 0:
        
        healed = False
        
        print("\nChoose action: 1. attack / 2. heal / 3. power")
        action = input("> ")
        
        if action == "attack":
            player_damage, p_cri = calculate_damage(
                player['min_dmg'],
                player['max_dmg']
            )
            
        elif action == "heal":
            healed = True
            heal_amount = int(player['max_hp'] * 0.2)
            player['hp'] += heal_amount
            if player['hp'] > player['max_hp']:
                player['hp'] = player['max_hp']
                
        else:
            if random.random() <= 0.7:
                player_damage, p_cri = calculate_damage(player['min_dmg'], player['max_dmg'])
                multiplier = random.uniform(1.5, 2.0)
                player_damage = int(player_damage * multiplier)
            else:
                print("You missed!")
                player_damage = 0
        
        monster_damage, m_cri = calculate_damage(
            monster["min_dmg"],
            monster["max_dmg"]
        )
        
        print("\nCurrent HP")
        print(f"Player: {player['hp']}, {monster_name}: {monster['hp']}")
        
        if healed == False:
            print(f"\nYou attacked a {monster_name}")
            if p_cri:
                print(f"Critical Hit! {player_damage} damage!")
            else:
                print(f"{player_damage} damage")
            monster['hp'] -= player_damage
            if monster['hp'] <= 0:
                print(f"\nYou defeated the {monster_name}!")
                player['xp'] += monster['xp']
                print(f"Gained {monster['xp']} XP!")
                return "win"
            
        print(f"\nYou were attacked by a {monster_name}")
        if m_cri:
            print(f"Critical Hit! {monster_damage} damage!")
        else:
            print(f"{monster_damage} damage")
        player['hp'] -= monster_damage
        if player['hp'] <= 0:
            return "game_over"
        
def calculate_damage(min_dmg, max_dmg):
    is_critical = False
    critical_rate = 0.1
    damage = random.randint(min_dmg, max_dmg)
    
    if random.random() <= critical_rate:
        is_critical = True
        damage *= 2
        return damage, is_critical
    
    else:
        return damage, is_critical
    
def check_level_up(player):
    required_xp = player['level'] * 20
    
    if player['xp'] >= required_xp:
        player['level'] += 1
        player['max_hp'] += 5
        player['min_dmg'] += 1
        player['max_dmg'] += 1
        player['hp'] = player['max_hp']
        print("\nLevel Up!")
        print(f"Level: {player['level']}\n")
        for stats, figure in player.items():
            print(f"{stats}: {figure}")