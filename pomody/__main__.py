import sys
from rich.console import Console
from pomody.pomody import pomody

console = Console()


class main:
    def __init__(self) -> None:
        if "-h" in sys.argv or "--help" in sys.argv:
            console.print(self.help())

        elif "-nm" in sys.argv or "--no-messages" in sys.argv:
            pomody(False)

        else:
            pomody()

    def help(self):
        var = """
            Usage:
                pomody [PARAMETERS]
            
            Parameters:
                -h, --help: Show this help
                -nm --no-messages: Disable messages
                """
        return var


if __name__ == "__main__":
    main()
