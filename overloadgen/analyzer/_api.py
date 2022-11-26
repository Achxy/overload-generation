from ast import parse, unparse
from inspect import getsource

from overloadgen.analyzer._analyze import OverloadNodeSourceGenerator
from overloadgen.analyzer._helpers import get_fn_from_module
from overloadgen.typing import get_overloads


def get_overload_nodes(func):
    overloads = get_overloads(func)
    nodes = [get_fn_from_module(parse(getsource(n))) for n in overloads]
    yield from OverloadNodeSourceGenerator(nodes).yield_overloads()


def get_overload_source(func):
    return "\n".join(unparse(node) for node in get_overload_nodes(func))
