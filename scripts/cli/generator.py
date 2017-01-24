from __future__ import print_function

import yaml
import click
import os
import shutil

from scripts.api_generator import APIGenerator
from scripts.cuba_enum_generator import CUBAEnumGenerator
from scripts.keywords_generator import KeywordsGenerator
from scripts.meta_class_generator import MetaClassGenerator
from scripts.validation_generator import ValidationGenerator


@click.group()
def cli():
    """ Auto-generate code from simphony-metadata yaml description. """


@cli.command()
@click.argument('yaml_file', type=click.File('rb'))
@click.argument('out_path', type=click.Path())
@click.option('-O', '--overwrite', is_flag=True, default=False,
              help='Overwrite OUT_PATH')
def meta_class(yaml_file, out_path, overwrite):
    """ Create the Simphony Metadata classes

    yaml_file:
        path to the simphony_metadata yaml file

    out_path:
        path to the directory where the output files should be placed

    overwrite:
        Allow overwrite of the file.
    """
    simphony_metadata_dict = yaml.safe_load(yaml_file)

    if os.path.exists(out_path):
        if overwrite:
            shutil.rmtree(out_path)
        else:
            raise OSError('Destination already exists: {!r}'.format(
                out_path))

    os.mkdir(out_path)

    meta_class_generator = MetaClassGenerator()
    meta_class_generator.generate(simphony_metadata_dict, out_path)
    api_generator = APIGenerator()
    api_generator.generate(simphony_metadata_dict, out_path)
    validation_generator = ValidationGenerator()
    validation_generator.generate(out_path)


@cli.command()
@click.argument('cuba_input', type=click.File('rb'))
@click.argument('cuds_input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def cuba_enum(cuba_input, cuds_input, output):
    """ Create the CUBA Enum

    cuba_input:
        Path to the cuba.yml

    cuds_input:
        Path to the simphony_metadata.yml

    output:
        Path to the output cuba.py file
    """
    cuba_dict = yaml.safe_load(cuba_input)
    simphony_metadata_dict = yaml.safe_load(cuds_input)

    generator = CUBAEnumGenerator()
    generator.generate(cuba_dict, simphony_metadata_dict, output)


@cli.command()
@click.argument('cuba_input', type=click.File('rb'))
@click.argument('cuds_input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def keywords(cuba_input, cuds_input, output):
    """ Create a dictionary of keywords.

    cuba_input:
        Path to the cuba.yml

    cuds_input:
        Path to the simphony_metadata.yml

    output:
        Path to the output keywords.py file
    """
    cuba_dict = yaml.safe_load(cuba_input)
    simphony_metadata_dict = yaml.safe_load(cuds_input)
    generator = KeywordsGenerator()
    generator.generate(cuba_dict, simphony_metadata_dict, output)