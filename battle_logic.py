def battle_logic(player, enemy):
    """
    Calculates the result of a turn of battle between the player and an enemy.
    """
    # Player goes first
    damage = player['attack'] - enemy['defense']
    enemy['health'] = max(enemy['health'] - damage, 0)
    if enemy['health'] <= 0:
        enemy['health'] = 0
        return player, enemy

    # Enemy attacks
    damage = enemy['attack'] - player['defense']
    player['health'] = max(player['health'] - damage, 0)
    if player['health'] < 0:
        player['health'] = 0
    return player, enemy
