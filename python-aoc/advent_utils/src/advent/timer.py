import cProfile
import pstats
import time
import subprocess
from typing import Callable, Literal
from advent.console import console


def solution_timer(year: int, day: int, part: int):
    prefix = _prefix(year, day, part)

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            try:
                start = time.perf_counter()
                solution = func(*args, **kwargs)

                if solution is None:
                    console.print("[red]No solution found[/red]")
                else:
                    print(solution)
                    # subprocess.run(["pbcopy"], input=str(solution), encoding="utf-8")
                    subprocess.run(["wl-copy"], input=str(solution), encoding="utf-8")

                diff = (time.perf_counter() - start) * 1000  # in milliseconds
            except Exception:
                console.print_exception()
            else:
                console.print(f"[green]{prefix}[white] {solution} [/white][yellow]{diff:.2f}ms[/yellow][/green]")
                return solution

        return wrapper

    return decorator


def solution_profiler(
    year: int,
    day: int,
    part: int,
    stats_amount: int = 5,
    sort: Literal["time", "cumulative"] = "time",
):
    prefix = _prefix(year, day, part)

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            with cProfile.Profile() as profiler:
                solution = func(*args, **kwargs)

            stats = pstats.Stats(profiler)

            if sort == "time":
                stats.sort_stats(pstats.SortKey.TIME)
            elif sort == "cumulative":
                stats.sort_stats(pstats.SortKey.CUMULATIVE)
            else:
                raise ValueError(
                    f"Invalid sort value: {sort}, expected 'time' or 'cumulative'"
                )

            stats.sort_stats(pstats.SortKey.TIME)
            console.print(f"Profiling [blue]{prefix}[/blue]")
            stats.print_stats(stats_amount)
            return solution

        return wrapper

    return decorator


def _prefix(year: int, day: int, part: int):
    return f"[blue]{year}-{day}-{part}[/blue]"
