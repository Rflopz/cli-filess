#!/usr/bin/python

import click
from Commands.Analize import analize

@click.group()
def cli():
    pass

cli.add_command(analize)

if __name__ == '__main__':
    cli()
