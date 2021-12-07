from crabs import (fuel_cost_for_moving_all, improve_solution,
                   is_optimal_target_position)

if __name__ == '__main__':
    h_positions = list(map(int, input().split(',')))

    # Given the nature of the geometric fuel consumption, we can assume that the
    # optimal position will be the average position, or it'll be close to it.
    average_h = sum(h_positions) // len(h_positions)
    optimal_h_position = average_h
    optimal_fuel_cost = fuel_cost_for_moving_all(h_positions, average_h)
    iterations = 0

    while not is_optimal_target_position(h_positions, optimal_h_position):
        iterations += 1
        optimal_h_position, optimal_fuel_cost = improve_solution(
            h_positions,
            optimal_h_position
        )

    print(f'Moving crabs to {optimal_h_position}, cost: {optimal_fuel_cost}')
    print(f'Solution found in {iterations} iterations')
