def get_next_state(game_map, current_state, action):
    if current_state not in game_map:
        return None
    
    if action in game_map[current_state]:
        return game_map[current_state][action]
    
    else:
        return None