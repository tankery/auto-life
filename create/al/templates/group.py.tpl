import click

{% for cli in clis %}from {{ cli | join('.') }}.cli import {{ cli | join('_') }}
{% endfor %}

@click.group()
def group(): pass

{% for cli in clis %}group.add_command({{ cli | join('_') }})
{% endfor %}
