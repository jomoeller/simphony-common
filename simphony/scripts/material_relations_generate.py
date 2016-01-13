import click
import yaml
from tabulate import tabulate
from collections import namedtuple

from simphony.core.keywords import KEYWORDS


def generate_class_import():
    return [
        "# code auto-generated by material_relations_generate.py\n",
        "from simphony.cuds.material_relations.material_relation import (\n",
        "\tMaterialRelation)\n",
        "from simphony.core.cuba import CUBA\n",
        "from simphony.core.cuds_material_relation import CUDSMaterialRelation\n"  # noqa
        "from simphony.core.data_container import DataContainer\n",
        "\n",
        "\n",
    ]


def generate_class_header(mr):
    return [
        "class {MR_NAME}(MaterialRelation):\n".format(
            MR_NAME=mr['class_name']
        ),
        "\n"
    ]


def generate_description_block(mr):
    return [
        "\t\"\"\" A {MR_NAME} material-relation\n".format(
            MR_NAME=mr['class_name']
        ),
        "\n",
        "\t{MR_DOC_DESCRIPTION}\n\n".format(
            MR_DOC_DESCRIPTION=mr['doc_description']
        ),
        "\tAttributes\n",
        "\t----------\n",
    ]


def generate_attributes_description(mr):

    code = []

    for param in mr['supported_parameters']:

        key = param['cuba'].split('.')[1]

        code += [
            "\t{ATT_NAME} : {ATT_TYPE}\n".format(
                ATT_NAME=param['cuba'].split('.')[1].lower(),
                ATT_TYPE=KEYWORDS[key].dtype
            ),
            "\t\t{ATT_DESC}\n".format(
                ATT_DESC=KEYWORDS[key].description
            ),
        ]

    return code


def generate_initializer(mr):

    code = []

    sub_param_cuba = ""

    code += [
        "\n\t\"\"\"  # noqa\n",
        "\n",
        "\tdef __init__(\n",
        "\t\tself,\n",
        "\t\tname,\n",
        "\t\tmaterials,\n",
        "\t\tdescription=\"\"",

    ]

    for param in mr['supported_parameters']:

        sub_param_cuba += "\n\t\t\t\t"+param['cuba']+","

        code += [
            ",\n",
            "\t\t{ATT_NAME}={ATT_DEF}".format(
                ATT_NAME=param['cuba'].split('.')[1].lower(),
                ATT_DEF=param['default']
            ),
        ]

    code += [
        "\n\t):\n",
        "\t\tsuper({MR_NAME}, self).__init__(\n".format(
            MR_NAME=mr['class_name']
        ),
        "\t\t\tname=name,\n",
        "\t\t\tdescription=description,\n",
        "\t\t\tkind=CUDSMaterialRelation.{MR_KEY},\n".format(MR_KEY=mr['key']),
        "\t\t\tmaterials=materials,\n",
        "\t\t\tparameters=DataContainer({\n"
    ]

    for param in mr['supported_parameters']:
        code += "\t\t\t\t{CUBA_KEY}: {ATT_NAME},\n".format(
            CUBA_KEY=param['cuba'],
            ATT_NAME=param['cuba'].split('.')[1].lower()
        )

    code += "\t\t\t})\n"
    code += "\t\t)\n"

    return code


def generate_property_get_set(mr):

    getter = (
        "\t@property\n"
        "\tdef {PROP_NAME}(self):\n"
        "\t\treturn self._parameters[{CUBA_KEY}]\n"
    )

    setter = (
        "\t@{PROP_NAME}.setter\n"
        "\tdef {PROP_NAME}(self, value):\n"
        "\t\tself._parameters[{CUBA_KEY}] = value\n"
    )

    get_set_block = getter + "\n" + setter

    lines = []

    for param in mr['supported_parameters']:
        lines.append("\n")
        lines.extend(get_set_block.format(
            PROP_NAME=param['cuba'].split('.')[1].lower(),
            CUBA_KEY=param['cuba']
        ))

    return lines


def generate_test_import(mr):
    lines = [
        "import unittest\n",
        "import uuid\n",
        "\n",
        "from simphony.cuds.material_relations.{} import (\n".format(
            mr['key'].lower()),
        "\t{})\n".format(mr['class_name']),
        "from simphony.testing.abc_check_material_relation import (\n",
        "\tCheckMaterialRelation)\n",
        "\n",
        "\n"
    ]

    return lines


def generate_test_header(mr):
    lines = [
        "class Test{MR_NAME}MaterialRelation(\n".format(
            MR_NAME=mr['class_name']
        ),
        "\tCheckMaterialRelation,\n",
        "\tunittest.TestCase\n",
        "):\n",
        "\tdef container_factory(\n",
        "\t\tself,\n",
        "\t\t\tname=\"{MR_NAME}\",\n".format(
            MR_NAME=mr['class_name']
        ),
        "\t\t\tmaterials=[uuid.uuid4() for _ in xrange({MR_NUM_MATS})]".format(
            MR_NUM_MATS=mr['allowed_number_materials'][0]
        ),
        "):\n",
        "\t\treturn {MR_NAME}(\n".format(
            MR_NAME=mr['class_name']
        ),
        "\t\t\tname=name,\n",
        "\t\t\tmaterials=materials\n",
        "\t\t)\n"
    ]

    return lines


def generate_test_parameters(mr):

    test_att_template = (
        "\tdef test_{ATT_NAME}(self):\n"
        "\t\trelation = self.container_factory('foo_relation')\n"
        "\n"
        "\t\tself.assertEqual(relation.{ATT_NAME}, {ATT_DEFAULT})\n"
    )

    test_update_att_template = (
        "\tdef test_{ATT_NAME}_update(self):\n"
        "\t\trelation = self.container_factory('foo_relation')\n"
        "\n"
        "\t\toriginal = relation.{ATT_NAME}\n"
        "\t\trelation.{ATT_NAME} = original + 1\n"
        "\n"
        "\t\tself.assertEqual(relation.{ATT_NAME}, original + 1)\n"
    )

    lines = []

    for param in mr['supported_parameters']:
        lines.append("\n")
        lines.extend(test_att_template.format(
            ATT_NAME=param['cuba'].split('.')[1].lower(),
            ATT_DEFAULT=param['default']
        ))
        lines.append("\n")
        lines.extend(test_update_att_template.format(
            ATT_NAME=param['cuba'].split('.')[1].lower(),
            ATT_DEFAULT=param['default']
        ))

    return lines


def generate_test_main():
    lines = [
        "\n",
        "if __name__ == '__main__':\n",
        "\tunittest.main()\n"
    ]

    return lines


@click.group()
def cli():
    """ Auto-generate code from material-relation yaml description. """


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('outpath', type=click.Path(exists=True))
def python(input, outpath):
    """ Create the material-relation classes.
    """
    material_relations = yaml.safe_load(input)

    for mr in material_relations:
        class_name_l = mr['key'].lower()
        with open(outpath+class_name_l+'.py', 'w+') as mrFile:
            lines = []
            lines += generate_class_import()
            lines += generate_class_header(mr)
            lines += generate_description_block(mr)
            lines += generate_attributes_description(mr)
            lines += generate_initializer(mr)
            lines += generate_property_get_set(mr)

            mrFile.writelines([i.replace('\t', '    ') for i in lines])


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('outpath', type=click.Path(exists=True))
def test(input, outpath):
    """ Create the material-relation test classes.
    """
    material_relations = yaml.safe_load(input)

    for mr in material_relations:
        class_name_l = mr['key'].lower()
        with open(outpath+"test_"+class_name_l+'.py', 'w+') as mrFile:
            lines = []
            lines += generate_test_import(mr)
            lines += generate_test_header(mr)
            lines += generate_test_parameters(mr)
            lines += generate_test_main()

            mrFile.writelines([i.replace('\t', '    ') for i in lines])


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def create_enum(input, output):
    """ Create the CUDSMaterialRelation Enum.
    """
    keywords = yaml.safe_load(input)

    lines = [
        '# auto-generated by the material_relations_generate.py script.\n',
        'from enum import IntEnum, unique\n',
        '\n',
        '\n',
        '@unique\n',
        'class CUDSMaterialRelation(IntEnum):\n',
        '\n']
    template = "    {} = {}\n"
    for keyword in keywords:
        lines.append(template.format(keyword['key'], keyword['number']))
    output.writelines(lines)


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def material_relations_definitions_py(input, output):
    """ Create a dictionary describing material relations.
    """
    keywords = yaml.safe_load(input)

    lines = [
        '# code auto-generated by the material_relations_generate.py script.\n',  # noqa
        'from collections import namedtuple\n',
        '\n',
        'from simphony.core.cuba import CUBA\n',
        'from simphony.core.cuds_material_relation import CUDSMaterialRelation\n'  # noqa
        '\n',
        '\n',
        'ATTRIBUTES = [\n'
        '    "number", "class_name", "allowed_number_materials",\n'
        '    "doc_description", "supported_parameters"]\n'
        'Material_Relation_Definition = namedtuple("Material_Relation_Definition",\n',  # noqa
        '                                          ATTRIBUTES)\n',  # noqa
        '\n',
        'Parameter = namedtuple("Parameter", ["cuba_key", "default_value"])\n',
        '\n',
        '\n',
        'MATERIAL_RELATION_DEFINITIONS = {\n']
    template = (
        "    CUDSMaterialRelation.{key}: Material_Relation_Definition(\n"
        "        class_name='{class_name}',\n"
        "        number={number},\n"
        "        allowed_number_materials={allowed_number_materials},\n"
        "        doc_description='{doc_description}',  # noqa\n"
        "        supported_parameters=[{supported_parameters} ]\n"
        "     ),\n")
    parameter_template = (
        "\n"
        "             Parameter(cuba_key={CUBA},\n"
        "                       default_value={DEFAULT}),")

    for keyword in keywords:
        parameters_list = ''
        for parameter in keyword['supported_parameters']:
            parameters_list += parameter_template.format(
                CUBA=parameter['cuba'],
                DEFAULT=parameter['default'])
        keyword['supported_parameters'] = parameters_list
        lines.extend(template.format(**keyword))
    lines.append('}\n')

    output.writelines(lines)


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def create_api(input, output):
    """ Create an rst document to describe api of the material relations.

    """
    keywords = yaml.safe_load(input)

    lines = [
        '.. auto-generated by material_relations_generate.py script.\n'
        '.. rubric:: Material relations\n\n',
        '.. currentmodule:: simphony.cuds.material_relations\n\n',
        '.. autosummary::\n\n']
    template = "   ~{}.{}\n"
    for keyword in keywords:
        lines.append(template.format(keyword['key'].lower(),
                                     keyword['class_name']))
    lines += '\n.. rubric:: Implementation\n\n'
    template = ("\n.. automodule:: simphony.cuds.material_relations.{}\n"
                "   :members:\n"
                "   :undoc-members:\n"
                "   :show-inheritance:\n")
    for keyword in keywords:
        lines.append(template.format(keyword['key'].lower()))
    output.writelines(lines)

_Column = namedtuple('_Column', ["key", "header", "formatter"])


@cli.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def table_rst(input, output):
    """ Create an rst document with table of different material relations.
    """
    keywords = yaml.safe_load(input)

    def format_supported_parameters(parameters):
        return ', '.join(["{}".format(param['cuba']) for param in parameters])

    columns = [_Column("key", "Key", lambda x: "{}".format(x)),
               _Column("class_name", "Class",
                       lambda x: ":class:`~.{}`".format(x)),
               _Column("doc_description", "Description",
                       lambda x: "{}".format(x)),
               _Column("allowed_number_materials",
                       "Allowed lengths of materials",
                       lambda x: "{}".format(x)),
               _Column("supported_parameters",
                       "Supported parameters",
                       format_supported_parameters)]

    table_header = [col.header for col in columns]
    table_header.append("Supported parameters")

    table_data = []

    for keyword in keywords:
        row = [col.formatter(keyword[col.key]) for col in columns]
        table_data.append(row)

    rst = tabulate(table_data, table_header, tablefmt="rst")
    output.write(
        ".. auto-generated by material_relations_generate.py script.\n\n")
    output.write(rst)


if __name__ == '__main__':
    cli()
