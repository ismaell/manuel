from __future__ import absolute_import
import click
from manuel.manuel import generate_report
from manuel.manuel import create_index


@click.group()
def manuel():
    pass


def invoke():
    manuel()


@manuel.command()
@click.argument('config_file')
@click.option('--index/--no-index', default=False)
@click.option('--debug/--no-debug', default=False)
@click.option('--name')
def cli_generate_report(config_file, index, debug, name):
    """
    CLI entry point

    :param config_file:
    :param index:
    :param debug:
    :return:
    """
    if index:
        create_index(config_file, debug)
    if not name:
        from os.path import basename, splitext
        name = splitext(basename(config_file))[0] or 'report'
    generate_report(config_file, debug, name)
