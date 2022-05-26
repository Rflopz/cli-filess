import click
from App.application import Application

@click.group()
def Analize():
    pass

@Analize.command()
@click.option('-p', '--path', help='Path to the folder to analize')
def all(path):
    Application.hello(path)