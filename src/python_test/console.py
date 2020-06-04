import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option(
    "-l",
    "--language",
    default="en",
    help="Wikipedia language.",
    metavar="LANG",
    show_default=True,
)
def main(language: str) -> None:
    """Python test project."""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
