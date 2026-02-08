from game_map import game_map
from engine import get_next_state

def run_game():
    current_state = "start"
    
    while True:
        print(f"\nYou are at: {current_state}")
        
        if current_state in ["treasure", "game_over", "monster"]:
            if current_state == "treasure":
                print("\nYou found a treasure!")
                break
            
            elif current_state == "game_over":
                print("\nGame Over")
                break
            
            else:
                print("\nYou were attacked by a monster!")
                break
            
        actions = game_map[current_state].keys()
        
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