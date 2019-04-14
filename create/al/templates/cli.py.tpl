import click

@click.command('{{ name }}')
def {{ function_name }}():
    '''{{ description }}'''
    click.echo()
    click.echo('Executing AL command {{ name }}')
