from distutils.core import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pomody",  # How you named your package folder (MyLib)
    packages=["pomody"],  # Chose the same as "name"
    version="0.5",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A pomodoro CLI app",  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Teko",  # Type in your name
    author_email="tekofxx@gmail.com",  # Type in your E-Mail
    url="https://github.com/Tekofx/pomody",  # Provide either the link to your github or to your website
    download_url="https://github.com/Tekofx/pomody/archive/refs/tags/",  # I explain this later on
    keywords=[
        "pomodoro",
        "productivity",
        "time",
        "timer",
        "work",
    ],
    install_requires=[
        "rich",
        "plyer",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "pomody=pomody.__main__:main",
        ]
    },
)
