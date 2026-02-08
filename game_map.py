game_map = {
    "start": {
        "look": "forest",
        "sleep": "game_over"
    },
    "forest": {
        "explore": "cave",
        "run": "start"
    },
    "cave": {
        "open_chest": ["treasure", "monster"],
        "leave": "forest"
    },
    "treasure": {},
    "game_over": {},
    "monster" : {},
    "win": {}
}
