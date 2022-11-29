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
from collections.abc import Callable, Iterable
from typing import Generic

from overloadgen._typeshack import Fn, P, R


class OverloadSignatureStore(Generic[P, R]):
    def __init__(
        self, function: Callable[P, R], signatures: Iterable[Callable] = ()
    ) -> None:
        self.function = function
        self._signatures: list[Callable] = list(signatures)

    def __call__(self, *args: P.args, **kwds: P.kwargs) -> R:
        return self.function(*args, **kwds)

    def overload(self, func: Fn) -> Fn:
        self._signatures.append(func)
        return func

    def clear_overloads(self) -> None:
        self._signatures.clear()

    def get_overloads(self):
        return self._signatures
