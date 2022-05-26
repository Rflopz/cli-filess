import click

@click.group()
def analize():
    pass

@analize.command()
@click.option('-p', '--path', help='Path to the folder to analize')
def all(path):
    click.echo('path %s' % path)