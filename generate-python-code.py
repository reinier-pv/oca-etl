import json
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

with open("input-requirements.json") as data_file:
    requirements = json.load(data_file)
    transforms = requirements['transforms']

    if len(transforms.items()) > 0:
        template = env.get_template('transformation_base_template.j2')
        output = template.render(table_headers=requirements['headers'], transforms=transforms)
        with open(requirements['table_name'] + "_transformation.py", "w") as fh:
            fh.write(output)
    else:
        print("TRANSFORMATIONS NOT FOUND")
