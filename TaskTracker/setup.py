from setuptools import setup

setup(
    name="taskcli",
    version="1.0",
    packages=["taskcli"],
    entry_points={
        "console_scripts": ["taskcli = taskcli.__main__:main"],
    },
    description="A CLI task management using argparser",
    author="Rajendra Katuwal",
    url="no url yet",
    python_requires=">=3.10",
)
