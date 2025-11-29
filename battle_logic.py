def battle_logic(player, enemy):
    """
    Calculates the result of a turn of battle between the player and an enemy.
    """
    # Player goes first
    damage = max(player['attack'] - enemy['defense'], 0)
    enemy['health'] -= damage
    if enemy['health'] <= 0:
        enemy['health'] = 0
        return player, enemy

    # Enemy attacks
    damage = max(enemy['attack'] - player['defense'], 0)
    player['health'] -= damage
    if player['health'] < 0:
        player['health'] = 0
    return player, enemy
