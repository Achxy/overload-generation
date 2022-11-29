"""
MIT License

Copyright (c) 2022 Achxy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
