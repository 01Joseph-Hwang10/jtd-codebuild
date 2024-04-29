import click
from ._logger import Logger


class ClickLogger(Logger):
    def debug(self, message: str, *args, **kwargs) -> None:
        kwargs.setdefault("color", "blue")
        message = f"[jtd-codebuild] | DEBUG | {message}"
        click.echo(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs) -> None:
        message = f"[jtd-codebuild] | INFO | {message}"
        click.echo(message, *args, **kwargs)

    def success(self, message: str, *args, **kwargs) -> None:
        message = f"[jtd-codebuild] | SUCCESS | {message}"
        kwargs.setdefault("color", "green")
        click.echo(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs) -> None:
        message = f"[jtd-codebuild] | WARNING | {message}"
        kwargs.setdefault("color", "yellow")
        click.echo(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs) -> None:
        message = f"[jtd-codebuild] | ERROR | {message}"
        kwargs.setdefault("color", "red")
        click.echo(message, *args, **kwargs)
