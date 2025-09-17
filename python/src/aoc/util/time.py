from typing import Callable, ParamSpec, TypeVar, overload

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


@overload
def timed(func: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> tuple[R, str]: ...


@overload
def timed(func: Callable[P, R]) -> Callable[P, tuple[R, str]]: ...


def timed(func: Callable, *args, **kwargs):
    def format_duration(seconds: float) -> str:
        if seconds >= 1:
            return f"{seconds:.3f} s"
        elif seconds >= 1e-3:
            return f"{seconds * 1e3:.3f} ms"
        elif seconds >= 1e-6:
            return f"{seconds * 1e6:.3f} µs"
        else:
            return f"{seconds * 1e9:.3f} ns"

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = format_duration(end - start)
        return result, elapsed

    return wrapper(*args, **kwargs) if args or kwargs else wrapper
