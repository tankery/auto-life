import click
import create

__author__ = "Tankery Chen"

main = click.CommandCollection(sources=[create.group])
