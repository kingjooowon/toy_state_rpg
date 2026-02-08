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