from collections import Counter

from fish import total_fish_produced

simulation_days = 256


if __name__ == '__main__':
    fish_timers = [int(n) for n in input().strip().split(',')]
    fish_timers_count = Counter(fish_timers)
    total_fish_count = len(fish_timers)

    for timer, count in fish_timers_count.items():
        fish_produced = total_fish_produced(timer, simulation_days)
        total_fish_count += count * fish_produced

    print(f'Total fish after {simulation_days} days: {total_fish_count}')
