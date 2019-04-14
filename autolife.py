import click

__author__ = "Tankery Chen"

# import all packages
from os.path import dirname, isdir, isfile, join
from os import listdir
dirs = listdir(dirname(__file__))
modules = [ __import__(f) for f in dirs if isdir(f) and isfile(join(f, '__init__.py'))]

main = click.CommandCollection(
    sources=[getattr(g, 'group') for g in modules if hasattr(g, 'group')],
    help="AL Automate your Life!")
