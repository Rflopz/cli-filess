#!/usr/bin/python

import click
from Commands.analize import Analize

@click.group()
def cli():
    pass

cli.add_command(Analize)

if __name__ == '__main__':
    cli()
