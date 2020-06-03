import textwrap

import click
import requests

from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option("-l", "--language", default="en", help="Wikipedia language.")

def main(language):
    """Python test project."""
    API_URL = "https://" + language + ".wikipedia.org/api/rest_v1/page/random/summary"

    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
