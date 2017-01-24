class CUBAEnumGenerator(object):
    """Generator class for cuba.py enumeration.
    """

    def generate(self, cuba_dict, simphony_metadata_dict, output):
        """Generates the cuba file from the yaml-extracted dictionary
        of cuba and simphony_metadata files. Writes the generated code
        in the file object output
        """
        lines = [
            '# code auto-generated by the\n',
            '# simphony-metadata/scripts/generate.py script.\n',
            '# cuba.yml VERSION: {}\n'.format(cuba_dict['VERSION']),
            'from enum import Enum, unique\n',
            '\n',
            '\n',
            '@unique\n',
            'class CUBA(Enum):\n'
            ]
        template = '    {keyword} = "{keyword}"\n'

        all_keys = set(
            cuba_dict['CUBA_KEYS']) | set(simphony_metadata_dict['CUDS_KEYS'])

        for keyword in sorted(list(all_keys)):
            lines.append(template.format(keyword=keyword))

        output.writelines(lines)