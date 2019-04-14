import click
from create.al.cli import create_al

@click.group()
def group(): pass

group.add_command(create_al)
