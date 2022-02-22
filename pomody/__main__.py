import sys
from rich.console import Console
from pomody.pomody import pomody

console = Console()


class main:
    def __init__(self) -> None:
        if "-h" in sys.argv or "--help" in sys.argv:
            console.print(self.help())
        activities = 3
        notifications = True

        if "-n" in sys.argv or "--no-notifications" in sys.argv:
            notifications = False

        if "-a" in sys.argv:
            activities = int(sys.argv[sys.argv.index("-a") + 1])
        if "--activities" in sys.argv:
            activities = int(sys.argv[sys.argv.index("--activities") + 1])
        print(activities)
        pomody(notifications, activities)

    def help(self):
        var = """
            Usage:
                pomody [PARAMETERS]
            
            Parameters:
                -h, --help: Show this help
                -n, --no-notifications: Disable notifications
                -a, --activities: Number of activities before a long break
                """
        return var


if __name__ == "__main__":
    main()
