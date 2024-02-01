from unittest.mock import mock_open, patch

"""Test file for code audit tools."""
from subprocess import CompletedProcess

import pytest
from tools.code_audit import read_config, run_command


# TO DO
def test_fmt() -> None:
    """test function for unit test"""
    project = "."
    assert type(project) == str


pyproject_data = """
[tool.poetry]
name = "taggenerator"
version = "0.1.0"
description = ""
authors = ["Tatiana <tatiana.ekeinhor@gmail.com>"]
readme = "README.md"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""


@pytest.mark.parametrize(
    "filename,expected",
    [("pyproject.toml", "taggenerator")],
)
@patch(
    "builtins.open", new_callable=mock_open, read_data=pyproject_data.encode("utf-8")
)  # the encoding gives a bytes, because the open read in `rb`` mode
def test_read_config(mock_file, filename, expected):
    actual = read_config(filename)
    mock_file.assert_called_with(filename, "rb")
    assert actual == expected


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_config_filenotfound(mock_file):
    filename = "unexistent.toml"
    expected = ""
    actual = read_config(filename)
    mock_file.assert_called_with(filename, "rb")
    assert actual == expected


pylama_dict = {"command": ["pylama", "--options", "pyproject.toml"]}
mypy_dict = {"command": ["mypy", "--config-file", "pyproject.toml"]}


@pytest.mark.parametrize(
    "cmd,project,args,return_code",
    [
        ({"pylama": pylama_dict}, "", ["pylama", "."], 0),
        ({"mypy": mypy_dict}, "", ["mypy", "."], 0),
        ({"mypy": mypy_dict}, "", ["mypy", "."], 1),
    ],
)
@patch("tools.code_audit.subprocess.run")
def test_run_command(mocked_subprocess_run, cmd, args, project, return_code):
    mocked_subprocess_run.return_value = CompletedProcess(args=args, returncode=return_code)
    with pytest.raises(SystemExit) as error:
        run_command(cmd, project)
    assert error.type == SystemExit
    assert error.value.code == return_code
