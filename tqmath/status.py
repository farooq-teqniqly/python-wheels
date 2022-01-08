from enum import IntEnum, unique


@unique
class ExitStatus(IntEnum):
    ERROR_CTRL_C = 130
