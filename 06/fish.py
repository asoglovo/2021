from functools import cache


spawned_fish_timer = 8
cycle_duration = 7


def total_fish_produced(fish_timer, simulation_duration):
    """
    Computes the total number of fish produced by a fish with the given timer.
    This sum includes all generations and sub-generations of this fish.
    """
    days = spawn_days_from_timer(fish_timer, simulation_duration)
    return len(days) + sum(
        [total_fish_produced_from_start_day(day, simulation_duration)
         for day in days]
    )


@cache
def total_fish_produced_from_start_day(day, simulation_duration):
    """
    Given the day where a new fish spawns and the simulation duration, computes
    the total number of produced fish by this fish and all its sub-generations.
    """
    next_gen_days = spawn_days_from_start_day(day, simulation_duration)

    return len(next_gen_days) + sum(
        [total_fish_produced_from_start_day(day, simulation_duration)
         for day in next_gen_days]
    )


def spawn_days_from_start_day(start_day, simulation_duration):
    """
    Given the day when a new fish has been spawned, it computes all the days
    where this fish would produce new fish in the simulation.
    """
    return spawn_days_from_timer(
        spawned_fish_timer,
        simulation_duration,
        start_day
    )


def spawn_days_from_timer(fish_timer, simulation_duration, start_day=0):
    """
    Given the initial timer of a fish, it returns a list of the simulation days
    where a new fish would be produced by this one.

    If the fish doesn't start on the first day of the simulation, the start_day
    parameter needs to be specified to indicate the day where the fish starts.

    start_day = 1 would means that the fish starts on the second day of the simulation
    (after one day is elapsed).
    """
    day_of_first_cycle = start_day + fish_timer + 1

    return list(
        range(day_of_first_cycle, simulation_duration + 1, cycle_duration)
    )
