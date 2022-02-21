import sys
from rich.console import Console
from pomo import pomopy

console = Console()


class main:
    def __init__(self) -> None:
        print("a")
        if "-h" in sys.argv or "--help" in sys.argv:
            console.print(self.help())

        else:
            pomopy()

    def help(self):
        var = """
            Usage:
                pomopy [PARAMETERS]
            
            Parameters:
                -h, --help: Show this help
                -nm --no-messages: Disable messages
                """
        return var


if __name__ == "__main__":
    main()
