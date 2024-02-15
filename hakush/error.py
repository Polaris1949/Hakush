class HakushError(RuntimeError):
    def __init__(self, message: str, url: str) -> None:
        super().__init__(f"{message} ({url})")
