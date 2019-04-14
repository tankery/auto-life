import click
import os

@click.command('create:al')
@click.option(
    '-n', '--name',
    help='Name of the cli',
    prompt='Name of the cli (use ":" to differentiate action and target. e.g. create:repo)')
@click.option(
    '-d', '--description',
    help='Description of the cli',
    prompt='Please write concise description')
def create_al(name: str, description: str):
    '''Create an AL command'''
    click.echo()
    click.echo('Creating AL command "%s": %s' %(name, description))

    # Find working directory
    work_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    click.echo('Working dir: %s' % work_dir)

    # Parse name
    cmd = name.replace('-', '_').split(':')

    # Check existence and validation
    valid, reson = _command_is_valid(work_dir, cmd)

    if not valid:
        click.echo('Error: %s' % reson, err=True)
        return

    # Create folder and generating code from template
    try:
        _generating(work_dir, cmd, name, description)
    except Exception as err:
        click.echo('Error: %s' % err, err=True)
        raise err


def _command_is_valid(_work_dir, _cmd):

    if len(_cmd) < 2:
        return False, 'Command should contains ":"'

    import re
    pattern = re.compile(r'^\w+$')
    for part in _cmd:
        if not pattern.match(part):
            return False, '"%s" is invalid command name part' % part
    
    path = os.path.join(_work_dir, *_cmd, 'cli.py')
    if os.path.exists(path):
        return False, 'Command exists in %s' % os.path.dirname(path)

    return True, ''


def _generating(_work_dir, _cmd, _name, _desc):
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    src = os.path.join(_work_dir, 'create', 'al', 'templates')
    dest = os.path.join(_work_dir, *_cmd)
    group = os.path.join(_work_dir, _cmd[0])
    env = Environment(
        loader=FileSystemLoader(src),
        autoescape=select_autoescape(['tpl'])
    )

    # Create dest folder if need
    os.makedirs(dest, exist_ok=True)

    # Generating cli.py
    click.echo('Generating cli.py in %s' % dest)
    template = env.get_template('cli.py.tpl')
    text = template.render(name=_name, description=_desc, function_name='_'.join(_cmd))

    with open(os.path.join(dest, 'cli.py'), 'w') as f:
        f.write(text)

    # Generating __init__.py in dest
    with open(os.path.join(dest, '__init__.py'), 'w') as f:
        f.write('')

    # (Re)generating __init__.py in group dir
    click.echo('(Re)generating __init__.py in %s' % group)

    paths = []
    for root, _, files in os.walk(group):
        for file in files:
            if file == 'cli.py':
                cmd_path = os.path.relpath(root, _work_dir)
                paths.append(cmd_path.split('/'))

    template = env.get_template('group.py.tpl')
    text = template.render(clis=paths)

    with open(os.path.join(group, '__init__.py'), 'w') as f:
        f.write(text)
