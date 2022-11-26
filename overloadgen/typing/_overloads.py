from collections import defaultdict
from collections.abc import Callable
from functools import partial

from overloadgen.typing._helpers import get_fn, mark_fallback, overload_dummy
from overloadgen.typing.errors import FunctionDidNotResolve

FALLBACK_OVERLOAD_REGISTRY = defaultdict(partial(defaultdict, dict))


@mark_fallback
def overload(func):
    fn = get_fn(func)
    if fn is None:
        raise FunctionDidNotResolve()
    module, qualname, code = fn.__module__, fn.__qualname__, fn.__code__
    FALLBACK_OVERLOAD_REGISTRY[module][qualname][code.co_firstlineno] = func
    return overload_dummy


@mark_fallback
def get_overloads(func) -> list[Callable]:
    fn = get_fn(func)
    if fn is None:
        raise FunctionDidNotResolve()
    module, qualname = fn.__module__, fn.__qualname__
    if module not in FALLBACK_OVERLOAD_REGISTRY or qualname not in (
        mapping := FALLBACK_OVERLOAD_REGISTRY[module]
    ):
        return list()
    return list(mapping[qualname].values())


@mark_fallback
def clear_overloads():
    FALLBACK_OVERLOAD_REGISTRY.clear()
