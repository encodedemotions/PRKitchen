import threading


class CookingAparatus:
    def __init__(self, name) -> None:
        self.is_available = True
        self.name = name