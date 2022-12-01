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
from ast import parse, unparse
from inspect import getsource

from ._analyze import OverloadNodeSourceGenerator
from ._helpers import get_fn_from_module
from ..overloading import get_overloads


def get_overload_nodes(func):
    overloads = get_overloads(func)
    nodes = [get_fn_from_module(parse(getsource(n))) for n in overloads]
    yield from OverloadNodeSourceGenerator(nodes).yield_overloads()


def get_overload_source(func):
    return "\n".join(unparse(node) for node in get_overload_nodes(func))
