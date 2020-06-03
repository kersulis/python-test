import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option("-l", "--language", default="en", help="Wikipedia language.")

def main(language):
    """Python test project."""
    data = wikipedia.random_page(language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
