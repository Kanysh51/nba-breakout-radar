players = {
    "Player A": [8.2, 15.7],
    "Player B": [12.1, 13.4],
    "Player C": [6.5, 14.0]
}

for player, points in players.items():
    improvement = points[1] - points[0]
    breakthrough=""
    if improvement>=5:
        breakthrough="yes"
    else:
        breakthrough="no"
    print(f"{player}/ {round(improvement, 1)} / 'breakthrough', {breakthrough}")