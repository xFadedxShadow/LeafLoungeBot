#!/usr/bin/env python3

# Classes
class Color:
    """
    Shares ANSI escape codes for color formatting
    """

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    B_RED = BOLD + RED
    B_GREEN = BOLD + GREEN
    B_YELLOW = BOLD + YELLOW
    B_BLUE = BOLD + BLUE
    B_MAGENTA = BOLD + MAGENTA
    B_CYAN = BOLD + CYAN
    B_WHITE = BOLD + WHITE
