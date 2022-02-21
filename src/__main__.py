import sys
from rich.console import Console

console = Console()


class main:
    def __init__(self) -> None:
        if "-h" in sys.argv or "--help" in sys.argv:
            console.print(self.help())

    def help(self):
        var = """
            Usage:
                pomopy [PARAMETERS]
            
            Parameters:
                -h, --help: Show this help
                -nm --no-messages: Disable messages
                """
        return var
