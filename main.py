#!/usr/bin/python

import click

@click.command()
def hello():
    click.echo('hello from click')

if __name__ == '__main__':
    hello()