import click

{% for cli in clis %}from {{ cli | join('.') }}.cli import {{ cli | join('_') }}
{% endfor %}
''' DO NOT EDIT THIS FILE
This is a generated file from template '/create/al/templates/group.py.tpl'
'''

@click.group()
def group(): pass

{% for cli in clis %}group.add_command({{ cli | join('_') }})
{% endfor %}
