"""Code audit tool for linting, formating and security checks."""
import subprocess
import tomllib
from typing import Dict, List

import click
from halo import Halo  # type: ignore # halo has missing lib that freaks mypy out

linters_cmd = {
    "pylama": {"command": ["pylama", "--options", "pyproject.toml"]},
    # "mypy": {"command": ["mypy"]},
}

security_cmd = {
    "bandit": {"command": ["bandit", "-c", "pyproject.toml", "-r"]},
}

fmt_cmd = {
    "black": {"command": ["black"]},
    "isort": {"command": ["isort"]},
}


def read_config() -> str:
    """Read pyproject in current directory and return the project name."""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        return data["tool"]["poetry"]["name"]  # type: ignore #toml.load returns a too generic type
    except FileNotFoundError:
        print("⛔️ Config file not found")
        return ""


def run_command(kwargs: Dict[str, Dict[str, List[str]]], project_name: str = "") -> None:
    """Run specified commands kwargs with subprocess."""
    if not project_name:
        project_name = read_config()

    for name, command in kwargs.items():
        spinner = Halo(text=f">> Running {name}...\n", spinner="arc", placement="right")
        spinner.start()
        result = subprocess.run(args=command["command"] + [project_name], check=False)
        if result.returncode == 0:
            spinner.succeed()
        else:
            spinner.fail()


@click.group()
def cli() -> None:
    """Command line groupe for audit tool."""


@click.command(name="fmt")
@click.option("-p", "--project", default=".")
def fmt(project: str) -> None:
    """Format the projet using black."""
    run_command(fmt_cmd, project)


@click.command(name="lint")
@click.option("-p", "--project", default=".")
def lint(project: str) -> None:
    """Apply all static checkers (linter) to the projet."""
    run_command(linters_cmd, project)


@click.command(name="secu")
@click.option("-p", "--project", default=".")
def secu(project: str) -> None:
    """Apply security checker to the projet."""
    run_command(security_cmd, project)


@click.command(name="all")
@click.option("-p", "--project", default=".")
def all_cmd(project: str) -> None:
    """Apply all checkers: linters, formatters and security."""
    run_command(linters_cmd | security_cmd | fmt_cmd, project)


cli.add_command(fmt)
cli.add_command(lint)
cli.add_command(secu)
cli.add_command(all_cmd)

if __name__ == "__main__":
    cli()
