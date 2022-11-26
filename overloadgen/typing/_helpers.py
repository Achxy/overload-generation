import typing
from collections.abc import Callable

from overloadgen.typing._constants import IS_GREATER_THAN_OR_EQ_311


def overload_dummy(*args, **kwds):
    """Helper for @overload to raise when called."""
    raise NotImplementedError(
        "You should not call an overloaded function. "
        "A series of @overload-decorated functions "
        "outside a stub module should always be followed "
        "by an implementation that is not @overload-ed."
    )


def get_fn(func: Callable) -> Callable:
    return getattr(func, "__func__", func)


def mark_fallback(fallback_fn: Callable):
    def inner(*args, **kwargs):
        if IS_GREATER_THAN_OR_EQ_311:
            fn = getattr(typing, fallback_fn.__name__)
            return fn(*args, **kwargs)
        return fallback_fn(*args, **kwargs)

    return inner
