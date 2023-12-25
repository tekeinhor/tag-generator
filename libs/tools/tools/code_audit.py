import tomllib
import subprocess
from typing import Dict, List
from halo import Halo
import click

linters_cmd = {
    "pylama": {"command": ["pylama"]},
    "mypy": {"command": ["mypy"]},
}

security_cmd = {
    "bandit": {"command": ["bandit"]},
}

fmt_cmd = {
    "black": {"command": ["black", "."]},
}


def read_config() -> str:
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        return data["tool"]["poetry"]["name"]
    except FileNotFoundError:
        print("⛔️ Config file not found")


def run_command(kwargs: Dict[str, Dict[str, List[str]]]):
    """Run all command"""
    project_name = read_config()
    for name, command in kwargs.items():
        spinner = Halo(text=f">> Running {name}...", spinner="arc", placement="right")
        spinner.start()
        result = subprocess.run(command["command"] + [project_name])
        if result.returncode == 0:
            spinner.succeed()
        else:
            spinner.fail()


@click.group()
def cli():
    pass


@click.command(name="fmt")
def fmt() -> None:
    """Format the projet using black."""
    run_command(fmt_cmd)


@click.command(name="lint")
def lint():
    """Apply all static checkers to the projet."""
    run_command(linters_cmd)


@click.command(name="secu")
def secu():
    """Apply all static checkers to the projet."""
    run_command(security_cmd)


@click.command(name="all")
def all():
    run_command(linters_cmd | security_cmd | fmt_cmd)


cli.add_command(fmt)
cli.add_command(lint)
cli.add_command(secu)
cli.add_command(all)

if __name__ == "__main__":
    cli()
