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
import typing
from collections.abc import Iterable
from types import FunctionType

from overloadgen._typeshack import All, ImplementationFunction, OverloadFunction
from overloadgen.typing._helpers import confirm_version
from overloadgen.typing._overloading import OverloadSignatureStore

__all__: All = (
    "signature_store",
    "get_overloads",
    "clear_overloads",
    "convert_to_signature_store",
)


def signature_store(function: FunctionType) -> OverloadSignatureStore:
    """
    Instantiate and return an `OverloadSignatureStore` which is structurually
    similar to `functools.singledispatch` but does not have any runtime effects.

    Args:
        function (FunctionType): The function implementation

    Returns:
        OverloadSignatureStore: Container holding implementation and overload functions
    """
    return OverloadSignatureStore(function)


def get_overloads(function: ImplementationFunction) -> Iterable[OverloadFunction]:
    """
    Reutrns an iterable of overloads for a given implementation function

    Args:
        function (ImplementationFunction): Implementation function

    Returns:
        Iterable[OverloadFunction]: Overload Functions
    """
    if isinstance(function, OverloadSignatureStore):
        return list(function.get_overloads())
    confirm_version()
    return getattr(typing, "get_overloads")(function)


def clear_overloads(function: ImplementationFunction) -> None:
    """
    Clears the available overloads for a given implementation function

    Args:
        function (Function): Implementation function
    """
    if isinstance(function, OverloadSignatureStore):
        function.clear_overloads()
    confirm_version()
    getattr(typing, "clear_overloads")()


def convert_to_signature_store(
    function: ImplementationFunction,
) -> OverloadSignatureStore:
    """
    Convert the given implementation function and return an `OverloadSignatureStore`
    if the implementation is already a signature store then a no-op return is performed

    Args:
        function (ImplementationFunction): Implementation function

    Returns:
        OverloadSignatureStore: Container holding implementation and overload functions
    """
    if isinstance(function, OverloadSignatureStore):
        return function
    signatures = get_overloads(function)
    return OverloadSignatureStore(function, signatures)
