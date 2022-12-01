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
from __future__ import annotations

import sys
from ast import AsyncFunctionDef, FunctionDef
from types import FunctionType
from typing import TYPE_CHECKING, Callable, Final, ParamSpec, TypeAlias, TypeVar

if TYPE_CHECKING:
    from .typing._overloading import OverloadSignatureStore
else:
    OverloadSignatureStore = TypeVar("OverloadSignatureStore")


Parameters = ParamSpec("Parameters")
Result = TypeVar("Result")
Fn = TypeVar("Fn", bound=FunctionType)

All: TypeAlias = tuple[str, ...]
Slots: TypeAlias = tuple[str, ...]

ImplementationFunction: TypeAlias = FunctionType | OverloadSignatureStore
OverloadFunction: TypeAlias = FunctionType | Callable
AnyFunctionDefinition: TypeAlias = FunctionDef | AsyncFunctionDef

OVERLOAD_RETRIEVAL_SUPPORTED: Final[bool] = sys.version_info >= (3, 11)
