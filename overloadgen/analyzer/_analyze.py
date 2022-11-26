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
