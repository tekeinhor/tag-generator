import tomllib
import subprocess
from typing import Dict, List
from halo import Halo
import click

linters_cmd = {
    "pylama": {"command": ["pylama", "--options", "pyproject.toml"]},
    "mypy": {"command": ["mypy"]},
}

security_cmd = {
    "bandit": {"command": ["bandit", "-c", "pyproject.toml", "-r"]},
}

fmt_cmd = {
    "black": {"command": ["black"]},
}



def read_config() -> str:
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        return data["tool"]["poetry"]["name"]
    except FileNotFoundError:
        print("⛔️ Config file not found")


def run_command(kwargs: Dict[str, Dict[str, List[str]]], project_name=None):
    """Run all command"""
    if not project_name:
        project_name = read_config()

    for name, command in kwargs.items():
        spinner = Halo(text=f">> Running {name}...", spinner="arc", placement="right")
        spinner.start()
        result = subprocess.run(args=command["command"] + [project_name])
        if result.returncode == 0:
            spinner.succeed()
        else:
            spinner.fail()


@click.group()
def cli():
    pass


@click.command(name="fmt")
@click.option("-p", "--project", default=".")
def fmt(project) -> None:
    """Format the projet using black."""
    run_command(fmt_cmd, project)


@click.command(name="lint")
@click.option("-p", "--project", default=".")
def lint(project):
    """Apply all static checkers to the projet."""
    run_command(linters_cmd, project)


@click.command(name="secu")
@click.option("-p", "--project", default=".")
def secu(project):
    """Apply all static checkers to the projet."""
    run_command(security_cmd, project)


@click.command(name="all")
@click.option("-p", "--project", default=".")
def all(project):
    run_command(linters_cmd | security_cmd | fmt_cmd, project)



cli.add_command(fmt)
cli.add_command(lint)
cli.add_command(secu)
cli.add_command(all)

if __name__ == "__main__":
    cli()
