from ast import FunctionDef, Module


def get_fn_from_module(module: Module) -> FunctionDef:
    (fndef,) = module.body
    if not isinstance(fndef, FunctionDef):
        msg = f"Expected parsed type to be of FunctionDef got {type(fndef)!r}"
        raise TypeError(msg)
    return fndef
