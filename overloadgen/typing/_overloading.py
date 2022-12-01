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
from typing import ClassVar, Generic

from overloadgen._typeshack import Fn, OverloadFunction, Parameters, Result, Slots


class OverloadSignatureStore(Generic[Parameters, Result]):
    """
    A container class for containing implementation function and
    it's overloads
    """

    __slots__: ClassVar[Slots] = ("function", "_signatures")

    def __init__(
        self,
        function: Callable[Parameters, Result],
        signatures: Iterable[OverloadFunction] = (),
    ) -> None:
        self.function = function
        self._signatures = list(signatures)

    def __call__(self, *args: Parameters.args, **kwds: Parameters.kwargs) -> Result:
        return self.function(*args, **kwds)

    def overload(self, func: Fn) -> Fn:
        """
        Mark the given function as an overload for the implementation function
        and reutrn it immediately

        Args:
            func (Fn): The overload function

        Returns:
            Fn: The same overload function after being marked as overload
        """
        self._signatures.append(func)
        return func

    def clear_overloads(self) -> None:
        """
        Clears the available overloads
        """
        self._signatures.clear()

    def get_overloads(self) -> Iterable[OverloadFunction]:
        """
        Returns an iterable of functions that were marked as overloads

        Returns:
            Iterable[OverloadFunction]: Functions that were marked as overloads
        """
        return self._signatures
