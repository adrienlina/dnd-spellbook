import csv

import yaml

output = []


def get_spell_fields(line):
    return {
        'level': int(line[0]),
        'name': line[1],
        'cast_type': line[3],
        'range': line[4],
        'description': line[7],
    }


with open('wizard.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')

    for line_number, line in enumerate(reader):
        output.append({
            'model': "spellbook.spell",
            'pk': line_number,
            'fields': get_spell_fields(line),
        })


with open('data.yml', 'w') as outfile:
    yaml.dump(output, outfile, default_flow_style=False)
