import click

__author__ = "Tankery Chen"

# import all packages
from os.path import dirname, isdir, isfile, join
from os import listdir
workdir = dirname(__file__)
dirs = listdir(workdir)
modules = [ __import__(f) for f in dirs if isdir(join(workdir, f)) and isfile(join(workdir, f, '__init__.py'))]

main = click.CommandCollection(
    sources=[getattr(g, 'group') for g in modules if hasattr(g, 'group')],
    help="AL Automate your Life!")
