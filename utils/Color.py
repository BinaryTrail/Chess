
class Color:
    def __init__(self):
        # Initialize Colors
        self.BLACK = '\033[30m'
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'
        self.CYAN = '\033[36m'
        self.LIGHT_GRAY = '\033[37m'
        self.DARK_GRAY = '\033[90m'
        self.BRIGHT_RED = '\033[91m'
        self.BRIGHT_GREEN = '\033[92m'
        self.BRIGHT_YELLOW = '\033[93m'
        self.BRIGHT_BLUE = '\033[94m'
        self.BRIGHT_MAGENTA = '\033[95m'
        self.BRIGHT_CYAN = '\033[96m'
        self.WHITE = '\033[97m'
        # Initialize Reset feature
        self.RESET = '\033[0m'  # called to return to standard terminal text color