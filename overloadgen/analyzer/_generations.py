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
from ast import FunctionDef, Name
from copy import deepcopy


class BaseGeneration:
    def __init__(
        self, overload: FunctionDef, *, default_annotation: Name | None
    ) -> None:
        ovargs = overload.args
        self.overload = overload
        self.ndefaultargs = len(ovargs.defaults)
        self.ndefaultkwargs = sum(value is not None for value in ovargs.kw_defaults)
        self.default_annotation = default_annotation
        self._make_new_base()

    def _make_new_base(self):
        self.base = deepcopy(self.overload)
        baseargs = self.base.args
        ovargs = self.overload.args
        baseargs.args = ovargs.args[: self.ndefaultargs - 1]
        baseargs.kwonlyargs = ovargs.kwonlyargs[: self.ndefaultkwargs - 1]
        baseargs.kw_defaults = []
        baseargs.defaults = []

    def default_args(self):
        args = self.overload.args
        keys = args.args[self.ndefaultargs - 1 :]
        values = args.defaults
        yield from zip(keys, values)

    def defaulted_kwonly_args(self):
        args = self.overload.args
        default = self.default_annotation
        keys = args.kwonlyargs[self.ndefaultkwargs - 1 :]
        values = [default if value is None else value for value in args.kw_defaults]
        yield from zip(keys, values)


class PossibilityGeneration:
    def __init__(
        self, overload: FunctionDef, *, default_annotation: Name | None
    ) -> None:
        self.overload = overload
        self.base = BaseGeneration(overload, default_annotation=default_annotation)

    def __iter__(self):
        fresh = deepcopy(self.base.base)
        yield fresh
        for arg, value in self.base.default_args():
            fresh.args.args.append(arg)
            fresh.args.defaults.append(value)
            yield fresh
        for kwarg, value in self.base.defaulted_kwonly_args():
            fresh.args.kwonlyargs.append(kwarg)
            fresh.args.kw_defaults.append(value)
            yield fresh
