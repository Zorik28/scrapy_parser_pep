from enum import Enum


class Pep(Enum):
    NAME = 1
    FOREPART = 0
    NUMBER = 1

    @classmethod
    @property
    def name(cls) -> int:
        return cls.NAME.value

    @classmethod
    @property
    def title_forepart(cls) -> int:
        return cls.FOREPART.value

    @classmethod
    @property
    def number(cls) -> int:
        return cls.NUMBER.value
