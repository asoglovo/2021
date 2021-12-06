from typing import List

spawned_fish_time = 8
restarted_fish_time = 6
simulation_days = 80


def tick_day(fish_timers: List[int]) -> List[int]:
    """
    Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while 
    each other number decreases by 1 if it was present at the start of the day.

    :param fish_timers: list of fish timers
    :return: new list of fish timers
    """
    new_fish_timers = [spawned_fish_time] * fish_timers.count(0)
    updated_timers = [
        restarted_fish_time if timer == 0 else timer - 1
        for timer in fish_timers
    ]

    return updated_timers + new_fish_timers


if __name__ == '__main__':
    fish_timers = [int(n) for n in input().strip().split(',')]

    for i in range(simulation_days):
        fish_timers = tick_day(fish_timers)

    print(f'After {simulation_days} days: {len(fish_timers)} fish')
