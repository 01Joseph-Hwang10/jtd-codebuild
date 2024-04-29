import click
from ._logger import Logger


class ClickLogger(Logger):
    def debug(self, message: str, *args, **kwargs) -> None:
        kwargs.setdefault("color", "blue")
        message = f"[DEBUG | jtd-codebuild] {message}"
        click.echo(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs) -> None:
        message = f"[INFO | jtd-codebuild] {message}"
        click.echo(message, *args, **kwargs)

    def success(self, message: str, *args, **kwargs) -> None:
        message = f"[SUCCESS | jtd-codebuild] {message}"
        kwargs.setdefault("color", "green")
        click.echo(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs) -> None:
        message = f"[WARNING | jtd-codebuild] {message}"
        kwargs.setdefault("color", "yellow")
        click.echo(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs) -> None:
        message = f"[ERROR | jtd-codebuild] {message}"
        kwargs.setdefault("color", "red")
        click.echo(message, *args, **kwargs)
