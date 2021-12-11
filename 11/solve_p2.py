from octopuses import read_octopuses_grid, simulate_octopuses_step, octopuses_count

max_iter = 1000

if __name__ == '__main__':
    input = read_octopuses_grid()

    did_all_octopuses_flash = False
    step = 0

    while not did_all_octopuses_flash:
        input, flashes = simulate_octopuses_step(input)

        did_all_octopuses_flash = flashes == octopuses_count
        step += 1

    print(f'All octupuses flashed at step: {step}')
