from . import utils


class KeywordsGenerator(object):
    """Generator for the keywords.py file."""
    def generate(self, cuba_dict, simphony_metadata_dict, output):
        """ Create a dictionary of keywords from the cuba and simphony_metadata
        yaml-extracted dictionaries. Writes the generated code in the file
        object output.
        """
        lines = [
            '# code auto-generated by the\n',
            '# simphony-metadata/scripts/generate.py script.\n',
            '# cuba.yml VERSION: {}\n'.format(cuba_dict['VERSION']),
            '# simphony_metadata.yml VERSION: {}\n'.format(
                    simphony_metadata_dict['VERSION']),
            'from collections import namedtuple\n',
            '\n',
            'import numpy\n',
            'import uuid  # noqa\n',
            '\n',
            '\n',
            'ATTRIBUTES = [\n'
            '    "name", "definition", "key", "shape", "length", "dtype"]\n'  # noqa
            'Keyword = namedtuple("Keyword", ATTRIBUTES)\n',
            '\n',
            '\n',
            'KEYWORDS = {\n']
        data_types = {
            'uuid': 'uuid.UUID',
            'string': 'numpy.str',
            'double': 'numpy.float64',
            'integer': 'numpy.int32',
            'boolean': 'bool'}
        template = (
            "    '{key}': Keyword(\n"
            "        name='{name}',\n"
            "        definition='{definition}',  # noqa\n"
            "        key='{key}',\n"
            "        shape={shape},\n"
            "        length={length},\n"
            "        dtype={type}),\n")
        for keyword, content in sorted(cuba_dict['CUBA_KEYS'].items(),
                                       key=lambda x: x[0]):
            content['type'] = data_types[content['type']]
            content['name'] = utils.to_camel_case(keyword)
            content['key'] = keyword
            content['shape'] = content.get("shape", [1])
            content['length'] = content.get("length", None)
            lines.extend(template.format(**content))

        for keyword, content in sorted(
                simphony_metadata_dict['CUDS_KEYS'].items(),
                key=lambda x: x[0]):
            content['type'] = "None"
            content['name'] = utils.to_camel_case(keyword)
            content['key'] = keyword
            content['shape'] = content.get("shape", [1])
            content['length'] = "None"
            lines.extend(template.format(**content))
        lines.append('}\n')

        output.writelines(lines)
