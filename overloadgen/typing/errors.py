class FunctionDidNotResolve(RuntimeError):
    def __init__(
        self,
        msg: str = "The __func__ attribute of the callable returned None",
    ) -> None:
        super().__init__(msg)
