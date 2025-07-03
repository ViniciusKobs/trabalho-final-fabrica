class PublicException(Exception):
    def __init__(
        self,
        msg = "error.internal.unknown",
        code = 500
    ):
        self.code = code
        super().__init__(msg)