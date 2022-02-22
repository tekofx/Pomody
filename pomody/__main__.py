import sys
from rich.console import Console
from pomody.pomody import pomody

console = Console()


class main:
    def __init__(self) -> None:
        if "-h" in sys.argv or "--help" in sys.argv:
            console.print(self.help())

        elif "-n" in sys.argv or "--no-notifications" in sys.argv:
            pomody(False)

        else:
            pomody()

    def help(self):
        var = """
            Usage:
                pomody [PARAMETERS]
            
            Parameters:
                -h, --help: Show this help
                -n --no-notifications: Disable notifications
                """
        return var


if __name__ == "__main__":
    main()
