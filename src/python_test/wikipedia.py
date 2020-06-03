import click
import requests


def random_page(language):
    API_URL = "https://" + language + ".wikipedia.org/api/rest_v1/page/random/summary"

    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
