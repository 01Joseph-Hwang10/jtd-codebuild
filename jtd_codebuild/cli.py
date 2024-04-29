import click
from click.core import Context
from .commands import BuildCommand, InitCommand


@click.group(invoke_without_command=True)
@click.argument("path", type=click.Path(), required=False)
@click.pass_context
def cli(ctx: Context, path: str):
    # If no subcommand is provided, run the build command
    if ctx.invoked_subcommand is None:
        BuildCommand().run(path or ".")
    else:
        ctx.obj = {"path": path}


@cli.command("init")
@click.pass_context
@click.option(
    "--preset",
    "-p",
    type=click.Choice(["config", "module", "workspace"]),
    default="config",
)
def init(ctx: Context, preset: str):
    path = ctx.obj["path"]
    InitCommand().run(path, preset)
