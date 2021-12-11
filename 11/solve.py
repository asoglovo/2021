from octopuses import read_octopuses_grid, simulate_octopuses_step

steps = 100

if __name__ == '__main__':
    input = read_octopuses_grid()
    flashes_count = 0

    for i in range(steps):
        input, flashes = simulate_octopuses_step(input)
        flashes_count += flashes

    print(f'Flashes count after {steps} steps: {flashes_count}')
