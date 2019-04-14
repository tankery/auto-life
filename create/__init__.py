import click
from create.al import create_al

@click.group()
def group():
    """
    Create awesome stuff
    """
    pass

group.add_command(create_al)
