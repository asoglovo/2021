def fuel_cost_for_moving(h_positions, target_position):
    """
    Calculates the fuel cost for moving all crabs from their horizontal position 
    to the target position.
    """

    return sum(
        [abs(h_pos - target_position) for h_pos in h_positions]
    )


if __name__ == '__main__':
    h_positions = list(map(int, input().split(',')))
    min_h, max_h = min(h_positions), max(h_positions)
    optimal_h_position, optimal_fuel_cost = None, float('inf')

    for target_position in range(min_h, max_h + 1):
        fuel_cost = fuel_cost_for_moving(h_positions, target_position)

        if fuel_cost < optimal_fuel_cost:
            optimal_h_position, optimal_fuel_cost = target_position, fuel_cost

    print(f'Moving crabs to {optimal_h_position}, cost: {optimal_fuel_cost}')
