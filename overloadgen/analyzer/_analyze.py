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
from ast import FunctionDef, Load, Name
from collections.abc import Iterable

from overloadgen.analyzer._generations import PossibilityGeneration


class OverloadNodeSourceGenerator:
    def __init__(
        self,
        overloads: Iterable[FunctionDef],
        default_annotation: str | None = "object",
    ) -> None:
        self.overlods = overloads
        self.default_annotation = (
            default_annotation
            if default_annotation is None
            else (Name(id=default_annotation, ctx=Load()))
        )

    def yield_overloads(self):
        for overload in self.overlods:
            yield from self.create_default_possibilities(overload)

    def create_default_possibilities(self, fndef: FunctionDef):
        yield from PossibilityGeneration(
            fndef, default_annotation=self.default_annotation
        )
