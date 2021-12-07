from functools import cache


def is_optimal_target_position(h_positions, target_position):
    """
    Checks if the target position is optimal.

    The position is optimal if the fuel cost for moving to any of its two sides
    is greater than the cost of the target position.
    """
    current_fuel_cost = fuel_cost_for_moving_all(h_positions, target_position)

    if fuel_cost_for_moving_all(h_positions, target_position - 1) < current_fuel_cost:
        return False

    if fuel_cost_for_moving_all(h_positions, target_position + 1) < current_fuel_cost:
        return False

    return True


def improve_target_position(h_positions, target_position):
    """
    Given the current target position, this function tries to improve it by
    looking for a contiguous position that minimizes the fuel cost for moving
    all crabs to that position.

    The function returns the new target position and its associated cost.
    """
    l_fuel_cost = fuel_cost_for_moving_all(h_positions, target_position - 1)
    r_fuel_cost = fuel_cost_for_moving_all(h_positions, target_position + 1)

    return (target_position - 1, l_fuel_cost) if l_fuel_cost < r_fuel_cost \
        else (target_position + 1, r_fuel_cost)


def fuel_cost_for_moving_all(h_positions, target_position):
    """
    Calculates the fuel cost for moving all crabs from their horizontal position 
    to the target position.
    """
    return sum(
        [fuel_cost_for_moving(h_pos, target_position) for h_pos in h_positions]
    )


@cache
def fuel_cost_for_moving(h_position, target_position):
    """
    Calculates the fuel cost for moving a crab from its horizontal position 
    to the target position.
    """
    return sum_until(abs(h_position - target_position))


def sum_until(n):
    """
    Calculates the sum of all numbers up to n: 1 + 2 + 3 + ... + n.
    """
    return sum(range(n + 1))
