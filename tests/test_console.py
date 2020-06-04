"""Test console module."""

from unittest.mock import Mock

import click.testing
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests

from python_test import console


@pytest.fixture
def runner() -> CliRunner:
    """Click runner fixture."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Use mocker for random_page."""
    return mocker.patch("python_test.wikipedia.random_page")


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It prints the Page title."""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It invokes requests.get."""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It uses English Wikipedia by default."""
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It exits with 1 when requests.get has an error."""
    mock_requests_get.side_effect = Exception("error")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It prints an error message when requests.get errors."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specified_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    """It uses the language passed with a given language code."""
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner: CliRunner) -> None:
    """It runs when it has access to the live Wikipedia API."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
