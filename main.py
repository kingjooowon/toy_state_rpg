from game_map import game_map
from engine import get_next_state, battle, check_level_up


def run_game():
    current_state = "start"
    player = {
        "hp": 20,
        "max_hp": 20,
        "xp": 0,
        "level": 1,
        "min_dmg": 3,
        "max_dmg": 7
    }
    
    while True:
        print(f"\nYou are at: {current_state}")
        
        if current_state in ["treasure", "game_over", "monster", "win"]:
            if current_state == "treasure":
                print("\nYou found a treasure!")
                print("\nGained 10 XP!")
                print("10% of your health has been restored")
                player['xp'] += 10
                player['hp'] += int(player['hp'] * 0.1)
                if player['hp'] > player['max_hp']:
                    player['hp'] = player['max_hp']
                    
                print(f"\nPlayer HP: {player['hp']}")
                    
                check_level_up(player)
                
                current_state = "forest"
                continue
            
            elif current_state == "game_over":
                print("\nGame Over")
                break
            
            elif current_state == "monster":
                    current_state = battle(player)
                    continue
                
            elif current_state == "win":
                print("\nYou won the battle!")
                print("30% of your health has been restored")
                player['hp'] += int(player['hp'] * 0.3)
                if player['hp'] > player['max_hp']:
                    player['hp'] = player['max_hp']
                    
                print(f"\nPlayer HP: {player['hp']}")
                
                check_level_up(player)
                
                current_state = "forest"
                continue
            
        actions = game_map[current_state].keys() # type: ignore
        
        print("Available actions:", " , ".join(actions))
        user_input = input("> ")
        
        next_state = get_next_state(game_map, current_state, user_input)
        if next_state is not None:
            current_state = next_state
            continue
        else:
            print("\nError")
        
if __name__ == "__main__":
    run_game()