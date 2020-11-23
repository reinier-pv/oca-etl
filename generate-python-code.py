import sys
import json
from jinja2 import Environment, FileSystemLoader

path_to_requirements = sys.argv[1]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

with open(path_to_requirements) as data_file:
    requirements = json.load(data_file)
    transforms = requirements['transforms']

    if len(transforms.items()) > 0:
        template = env.get_template('transformation_base_template.j2')
        output = template.render(table_file_path=requirements['table_file_path'], table_headers=requirements['headers'],
                                 transforms=transforms)
        print(output)
        with open("generated_transformation.py", "w") as fh:
            fh.write(output)
    else:
        print("TRANSFORMATIONS NOT FOUND")
