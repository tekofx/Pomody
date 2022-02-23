from typing import Text
from rich.progress import (
    track,
    Progress,
    BarColumn,
    TimeRemainingColumn,
    SpinnerColumn,
    TextColumn,
)
from time import sleep
import os
from pomody.console import Console

WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 30 * 60


class pomody:
    def __init__(self, notifications: bool = True, activities: int = 3) -> None:
        console = Console(notifications)

        count = 0
        while True:

            if count != activities:
                os.system("clear")
                self.progress_bar(WORK_TIME, "Working")
                os.system("clear")
                count += 1
                console.print(
                    "Working time has ended, would you like to take a break?: y/n"
                )
                var = input()
                os.system("clear")
                if var == "y":
                    self.progress_bar(SHORT_BREAK_TIME, "Break!")
                    os.system("clear")
                    console.print(
                        "Break has ended, press enter when you are ready to work again"
                    )
                    input()
            else:
                console.print(
                    "Congratulations! You have completed {} pomodoros, press enter to start long break".format(
                        activities
                    )
                )
                input()
                self.progress_bar(LONG_BREAK_TIME, "Long Break!")
                count = 0

    def progress_bar(self, time: int, description: str):
        with Progress(
            TextColumn(" "),
            "[progress.description ]{task.description}",
            SpinnerColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            BarColumn(bar_width=100),
            TimeRemainingColumn(),
            TextColumn(" "),
            expand=True,
        ) as progress:
            task1 = progress.add_task(description=description, total=time)
            while not progress.finished:
                progress.update(task1, advance=1)
                sleep(1)
